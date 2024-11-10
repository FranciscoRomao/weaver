from compilers.DPQA.solve import DPQA
from compilers.DPQA.animation import CodeGen
import argparse
import json
import pdb
import pandas as pd
from time import perf_counter
from math import e
from qiskit import QuantumCircuit
import os

gate_1q_fid = 0.999
gate_2q_fid = 0.995
gate_3q_fid = 0.98
gate_4q_fid = 0.95

gate_1q_time = 0.5
gate_2q_time = 0.2

t1_time = 100 * 10**6
t2_time = 1.5 * 10**6

qaoa_depth = 1

#instances_names = ['uf20-09.cnf',
#                    'uf20-010.cnf']

instances_names = ['uf3-01.cnf',
                    'uf3-02.cnf',
                    'uf3-03.cnf',
                    'uf3-04.cnf',
                    'uf3-05.cnf']

def run():

    basis_gates = ["rx", "rz", "x", "y", "z", "h", "id", "cz"]
    qaoas_instances = []
    transpiled_circuits = []

    results = pd.DataFrame(columns=['n_variables', 'qaoa_depth', '1q_gates', '2q_gates', 'compile_time', 'execution_time', 'eps'])

    for name in instances_names:
        variables = name.split('-')[0].replace('uf', '')
        variant = name.split('-')[1].replace('.cnf', '')

        with open(f'benchmarks/DPQA/graph{variables}_{variant}.json') as f:
            graphs = json.load(f)
   
            circuit_file = 'benchmarks/QASMBench/' + name.replace('.cnf', '.qasm')
            circuit = QuantumCircuit.from_qasm_file(circuit_file)
    
        tmp = DPQA(
            name=str(variables) + '_' + str(variant),
            dir='results/',
            print_detail=True
        )

        tmp.setArchitecture([16, 16, 16, 16])
        tmp.setProgram(graphs[str(variables)][0])
        tmp.setCommutation()
        tmp.hybrid_strategy()
        tmp.solve(save_file=True)

        compile_time = tmp.result_json['duration']

        filename = 'results/' + str(variables) + '_' + str(variant) + '.json'

        codegen = CodeGen(filename, dir='results/')

        codegen.builder(no_transfer=False).emit_full()

        with open(filename.replace('.json', '_code_full.json'), 'r') as f:
            full_code = json.load(f)

        total_execution_time = 0
        for i in full_code:
            total_execution_time += i['duration']

        total_execution_time += circuit.count_ops()['u3'] * 0.5

        print('total_execution_time:', total_execution_time)

        compile_time = float(tmp.result_json['duration'])

        t_busy = circuit.count_ops()['u3'] * 0.5 + circuit.count_ops()['cz'] * 0.2

        print('t_busy:', t_busy)

        t_idle = total_execution_time - t_busy

        print('t_idle:', t_idle)

        t_eff = t1_time*t2_time/(t1_time+t2_time)

        print('t_eff:', t_eff)

        tota_gate_fid = gate_1q_fid**circuit.count_ops()['u3'] * gate_2q_fid**circuit.count_ops()['cz']

        print('tota_gate_fid:', tota_gate_fid)

        eps = e**(-t_idle/t_eff)*tota_gate_fid

        print('eps:', eps)

        n_cz = 0

        for i in full_code:
            if 'Rydberg' in i['name']:
                n_cz += 1

        #runtime = compile_time + execution_time

        pdb.set_trace()

        #results.to_csv('./evaluation/results/dpqa_results.csv')

        results.loc[len(results)] = [variables, qaoa_depth, circuit.count_ops()['u3'], n_cz, compile_time, total_execution_time, eps]

    #if './evaluation/results/dpqa_results.csv' exists, append to it, else create it
    if not os.path.isfile('results/dpqa_results.csv'):
        results.to_csv('results/dpqa_results.csv')
    else:
        results.to_csv('results/dpqa_results.csv', index=False, mode='a', header=False)
