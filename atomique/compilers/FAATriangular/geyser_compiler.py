import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)
from time import time

import yaml

from compilers.FAATriangular.code.gen_qasm import geyser
from utils import count_layer, gen_res_dict, get_fid_and_time


class Geyser_Compiler:
    def __init__(self, configs):
        self.configs = configs

    def run(self, benchmark_sets, hyperparam_sets):

        res_list = []
        for benchmark in benchmark_sets.all_benchmarks:
            prev_compiled_circuit = None
            prev_time = 0
            compiled_time = 0
            for hyperparams in hyperparam_sets.all_sets:
                if hyperparams.retranspile or prev_compiled_circuit is None:
                    benchmark.circ.remove_final_measurements()
                    start = time()
                    compiled_circuit = geyser(benchmark.circ, hyperparams)
                    compiled_time = time() - start
                    prev_time = compiled_time
                    prev_compiled_circuit = compiled_circuit
                else:
                    compiled_time = prev_time
                    compiled_circuit = prev_compiled_circuit

                res_dict = gen_res_dict(
                    hyperparams, benchmark, compiled_circuit, device="na"
                )
                if hyperparams.geyser_use_blocking:
                    file_name = f"{hyperparam_sets.configs.result_path}/{benchmark.path.replace('/', '_')}_blocking.tranpiled"
                else:
                    file_name = f"{hyperparam_sets.configs.result_path}/{benchmark.path.replace('/', '_')}_no_blocking.tranpiled"
                if hyperparams.retranspile and hyperparams.geyser_dump_transpiled_qasm:
                    with open(file_name, "w") as file:
                        file.write(compiled_circuit.qasm())
                # res_dict['transpiled_qasm'] = benchmark.circ.qasm().replace('\n', ' ')

                res_dict["compilation_time"] = compiled_time
                res_dict["hyperparams"] = hyperparams.__dict__.copy()
                res_dict["path"] = benchmark.path

                res_list.append(res_dict)

                # print(res_dict)

                # yaml.dump(res_list, open(f"{hyperparam_sets.configs.result_path}/res.yml", "w"))
        yaml.dump(res_list, open(f"{hyperparam_sets.configs.result_path}/res.yml", "w"))
        return res_list
