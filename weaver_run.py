from pysat.formula import CNF
from compilers.weaver.compiler.entrypoint import Max3satQaoaCompiler
from compilers.weaver.nac.config import FPQAConfig
#from utils.hamiltonians import Max3satHamiltonian
#from utils.qaoa import QAOA
#from qiskit import transpile
import os
import pdb
import time
import pandas as pd
from compilers.weaver.utils.sat_utils import get_color_map

data = []
columns = [
    "name", 
    "num_variables", 
    "num_clauses", 
    "num_colors", 
    "compilation_time (seconds)", 
    "execution_time (microseconds)",
    "eps (fidelity)", 
    "#u3", 
    "#cz",
    "#ccz", 
    "ccz_fidelity", 
    "fpqa_config"
]

def run():
    ccz_fidelities = [0.9775, 0.98, 0.9825, 0.985, 0.9875, 0.99, 0.9925, 0.995, 0.9975]
    benchmarks = list(filter(lambda f: f.endswith(".cnf"), os.listdir("./benchmarks/max3SAT")))
    num_benchmarks = len(benchmarks)

    for index, filename in enumerate(benchmarks):
        fpqa_config = FPQAConfig({})
        print(f"Compiling {filename} ({index + 1}/{num_benchmarks})...")
        if not filename.endswith(".cnf"):
            continue
        formula = CNF(from_file=f"./benchmarks/max3SAT/{filename}")
        num_colors, color_map = get_color_map(formula)
        start_time = time.time()
        compiler = Max3satQaoaCompiler(formula, fpqa_config)
        program = compiler.compile_single_layer()
        execution_time = program.duration()
        gates = program.count_ops()
        end_time = time.time()
        compilation_time = end_time - start_time
        for ccz_fidelity in ccz_fidelities:
            program.fpqa.config.CCZ_GATE_FIDELITY = ccz_fidelity
            fidelity = program.avg_fidelity()
            row = [
                filename, 
                str(formula.nv), 
                str(len(formula.clauses)), 
                str(num_colors), 
                str(compilation_time), 
                str(execution_time), 
                str(fidelity), 
                str(gates["u3"]), 
                str(gates["cz"]), 
                str(gates["ccz"]), 
                str(ccz_fidelity), 
                fpqa_config.to_string()
            ]
            data.append(row)

    df = pd.DataFrame(data, columns=columns)
    df.to_csv("results/weaver_results.csv")