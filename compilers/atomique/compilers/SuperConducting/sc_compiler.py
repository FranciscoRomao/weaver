import os
import sys

import yaml

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)

from time import time

from qiskit import transpile
from qiskit.providers.fake_provider import FakeWashington

from utils import count_layer, gen_res_dict, get_fid_and_time


class SC_Compiler:
    def __init__(self, configs):
        self.configs = configs

    def run(self, benchmark_sets, hyperparam_sets):
        basis_gates = ["u3", "cx", "id", "u2", "u1"]
        # basis_gates = ["u3", "cx", "id"]
        backend = FakeWashington()
        cmap = backend.configuration().coupling_map
        res_list = []
        for benchmark in benchmark_sets.all_benchmarks:
            prev_compiled_circuit = None
            prev_compiled_time = 0
            compiled_time = 0
            for hyperparams in hyperparam_sets.all_sets:
                if hyperparams.retranspile or prev_compiled_circuit is None:
                    benchmark.circ.remove_final_measurements()
                    start = time()
                    compiled_circuit = transpile(
                        benchmark.circ,
                        coupling_map=cmap,
                        basis_gates=basis_gates,
                        optimization_level=3,
                        routing_method="sabre",
                        layout_method="sabre",
                        seed_transpiler=hyperparams.sc_seed_transpiler,
                    )
                    compiled_time = time() - start
                    prev_compiled_time = compiled_time
                    prev_compiled_circuit = compiled_circuit
                else:
                    compiled_circuit = prev_compiled_circuit
                    compiled_time = prev_compiled_time

                res_dict = gen_res_dict(hyperparams, benchmark, compiled_circuit, "sc")
                # print(res_dict)

                if hyperparams.retranspile:
                    with open(
                        f"{hyperparam_sets.configs.result_path}/{benchmark.path.replace('/', '_')}.tranpiled",
                        "w",
                    ) as file:
                        file.write(compiled_circuit.qasm())
                res_dict["compilation_time"] = compiled_time
                res_dict["hyperparams"] = hyperparams.__dict__.copy()
                res_dict["path"] = benchmark.path
                # res_dict['transpiled_qasm'] = benchmark.circ.qasm().replace('\n', ' ')
                res_list.append(res_dict)
                # yaml.dump(res_list, open(f"{hyperparam_sets.configs.result_path}/res.yml", "w"))

        yaml.dump(res_list, open(f"{hyperparam_sets.configs.result_path}/res.yml", "w"))
        return res_list
