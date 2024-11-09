import pdb
from copy import deepcopy
from multiprocessing import Pool
import pdb
import numpy as np
import yaml
from torchpack.utils.config import configs
from compilers.atomique.compilers.FPQAC.fpqac_generic_compiler import FPQACGenericCompiler
from compilers.atomique.benchmarks.benchmark_set import BenchmarkSets
from compilers.atomique.hyperparams import HyperParamSets
from compilers.atomique.utils import count_1q_2q_gates, get_n2q_interation_stats
import pandas as pd
from itertools import cycle

def run():
    configs.load("atomique_config.yml", recursive=True)
    configs.update([])

    #result_path = args_config.replace("configs", "results").replace(".yml", "")
    configs.result_path = "results"
    hyperparam_sets = HyperParamSets(configs)

    print("Loading Benchmarks...")
    benchmark_sets = BenchmarkSets(configs)

    file_name = str(benchmark_sets).split('/')[-1].split(']')[0].split('.')[0]

    if configs.get("count_gates", False):
        for benchmark in benchmark_sets.all_benchmarks:
            n_1q_gate, n_2q_gate = count_1q_2q_gates(benchmark.circ)
            stats = get_n2q_interation_stats(benchmark.circ)
            avg_2q = stats["n_2q_gate_qubit_list_mean"]
            avg_inter = stats["interact_qubit_list_mean"]
            print(f"& {n_2q_gate} & {n_1q_gate} & {avg_2q:.1f} & {avg_inter:.1f}")

    print("Start Compiling...")

    compiler = FPQACGenericCompiler(configs)
    
    all_res = compiler.run(
        benchmark_sets=benchmark_sets, hyperparam_sets=hyperparam_sets
    )

    #def numpy_array_representer(dumper, data):
    #    return dumper.represent_list(data.tolist())
    
    #pdb.set_trace()

    #yaml.add_representer(np.ndarray, numpy_array_representer)
    #yaml.dump(all_res, open(f"{hyperparam_sets.configs.result_path}/res_{file_name}.yml", "w"))
    #all_fid_list = []
    #all_2q_list = []
    #all_depth_list = []
    #all_time_list = []
    #for res in all_res:
    #    all_fid_list.append(res["fidelity"]["total_fidelity"])
    #    all_time_list.append(res["time"]["total_time"])
    #    if "circ_stats" in res.keys():
    #        all_2q_list.append(res["circ_stats"]["n_2q_gate"])
    #        all_depth_list.append(res["circ_stats"]["n_2q_layer"])
    #        all_time_list.append(res["time"]["total_time"])

    data = pd.DataFrame(columns=['variant', 'n_variables', 'depth', 'total_fidelity', 'compilation_time', 'n_1q_gate', 'n_2q_gate', 'execution_time'])

    yaml.dump(all_res, open(f"{hyperparam_sets.configs.result_path}/atomique_results.yml", "w"))

    pdb.set_trace()

    nqubits = all_res[0]['hyperparams']['configs']['benchmarks'][0]['n_qubits']
    types = all_res[0]['hyperparams']['configs']['benchmarks'][0]['type']
    
    for j, nqubit in enumerate(nqubits):
        for i, types_ in zip(all_res[j*len(types): (j+1)*len(types)], types):
            data.loc[len(data)] = [types_[0], nqubit, types_[1], i['fidelity']['total_fidelity'], i['circ_stats']['compilation_time'], i['circ_stats']['n_1q_gate'], i['circ_stats']['n_2q_gate'], i['time']['total_time']]
        
    #for i,type in zip(all_res,all_res[0]['hyperparams']['configs']['benchmarks'][0]['type']):
    #    data.loc[len(data)] = [type[0], all_res[0]['hyperparams']['configs']['benchmarks'][0]['n_qubits'][0], type[1], i['fidelity']['total_fidelity'], i['circ_stats']['compilation_time'], i['circ_stats']['n_1q_gate'], i['circ_stats']['n_2q_gate'], i['time']['total_time']]

    data.to_csv(f"{hyperparam_sets.configs.result_path}/atomique_results.csv")