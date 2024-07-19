import json
import time
from copy import deepcopy

import numpy as np
import yaml
from qiskit import QuantumCircuit, transpile

from utils import gen_res_dict

from .neutralatomcompilation import Hardware, InteractionModel, LookaheadCompiler
from .neutralatomcompilation.utilities.decompose_swaps import decompose_swap


class BakerCompiler(object):
    def __init__(self, configs):
        self.configs = configs

    def run(self, benchmark_sets, hyperparam_sets):
        res_list = []
        for benchmark in benchmark_sets.all_benchmarks:
            for hyperparams in hyperparam_sets.all_sets:
                res_dict = self.compile(benchmark, hyperparams)
                res_dict["hyperparams"] = hyperparams.__dict__.copy()
                res_dict["path"] = benchmark.path
                res_list.append(res_dict)
                #   analyzer = Analyzer(log, hyperparams)
                #   report = analyzer.analyze()
                print(res_dict)

        yaml.dump(res_list, open(f"{hyperparam_sets.configs.result_path}/res.yml", "w"))
        return res_list

    def compile(self, benchmark, hyperparams):
        start = time.time()
        circ = benchmark.circ

        n_rows = hyperparams.n_rows
        n_cols = hyperparams.n_cols
        n_aods = hyperparams.n_aods

        n_qubits = n_cols * n_rows * (n_aods + 1)
        n_rows_baker = n_cols_baker = int(np.floor(np.sqrt(n_qubits)))
        print(n_rows_baker, n_cols_baker)

        hw = Hardware(
            num_dimensions=2,
            dimensions_length=(n_rows_baker, n_cols_baker),
            dimensions_spacing=(1, 1),
        )
        im = InteractionModel(hardware=hw, d_to_r=lambda x: x / 2, max_int_dist=2)
        compiler = LookaheadCompiler(interaction_model=im, hardware=hw)

        circ_out = compiler.compile(
            circ,
            lookahead_distance=float("inf"),
            weighting_function=lambda x: np.e ** (-x),
        )
        circ_decomposed = decompose_swap(circ_out, hw, im, record_largest_gate=None)
        circ_cz = transpile(
            circ_decomposed,
            basis_gates=["cz", "u3", "u2", "u1", "id"],
            optimization_level=1,
        )

        #    count = circ_cz.count_ops()
        res_dict = gen_res_dict(hyperparams, benchmark, circ_cz, "baker")
        res_dict["compilation_time"] = time.time() - start

        #    log = {"n_gate_1q": count["u3"]+count["u2"]+count["u1"],
        #           "n_gate_2q": count["cz"],
        #           "depth": count["barrier"] + 1,
        #           "n_qubit": circ.num_qubits,
        #           "compilation_time": time.time() - start,
        #           }
        #    print(res_dict)
        return res_dict


def analyze(device_config, log):
    fid_2q = device_config["2Q_fidelity_long_range"]
    fid_1q = device_config["1Q_fidelity"]
    time_2q = device_config["2Q_time"]
    time_1q = device_config["1Q_time"]
    n_qubit = log["n_qubit"]
    T1 = device_config["T1"]

    n_gate_2q = log["n_gate_2q"]
    n_gate_1q = log["n_gate_1q"]
    time = time_2q * n_gate_2q + time_1q * n_gate_1q

    fidelity = fid_2q**n_gate_2q * fid_1q**n_gate_1q * np.exp(-time * n_qubit / T1)
    print(n_gate_1q, n_gate_2q)
    print(fid_1q**n_gate_1q, fid_2q**n_gate_2q, np.exp(-time * n_qubit / T1), fidelity)
    log["fidelity"] = fidelity
    log["time"] = time
    log["time_exec_over_decoherence"] = time / T1
    return log
