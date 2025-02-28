from compilers.DPQA.solve import DPQA
from compilers.DPQA.animation import CodeGen
import json
import pandas as pd
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

instances_names = ['uf20-01.cnf',
                    'uf20-02.cnf',
                    'uf20-03.cnf',
                    'uf20-04.cnf',
                    'uf20-05.cnf',
                    'uf20-06.cnf',
                    'uf20-07.cnf',
                    'uf20-08.cnf',
                    'uf20-09.cnf',
                    'uf20-010.cnf']

def run():

    results = pd.DataFrame(columns=['n_variables', 'qaoa_depth', '1q_gates', '2q_gates', 'compile_time', 'execution_time', 'eps'])

    for name in instances_names:
        print(f"Transpiling circuit {name.replace('.cnf', '.qasm')}")
        variables = name.split('-')[0].replace('uf', '')
        variant = name.split('-')[1].replace('.cnf', '')

        with open(f'benchmarks/DPQA/graph{variables}_{variant}.json') as f:
            graphs = json.load(f)
   
            circuit_file = 'benchmarks/QASMBench/' + name.replace('.cnf', '.qasm')
            circuit = QuantumCircuit.from_qasm_file(circuit_file)
    
        tmp = DPQA(
            name=str(variables) + '_' + str(variant),
            dir='results/',
            print_detail=False
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

        t_idle = total_execution_time - t_busy

        t_eff = t1_time*t2_time/(t1_time+t2_time)

        tota_gate_fid = gate_1q_fid**circuit.count_ops()['u3'] * gate_2q_fid**circuit.count_ops()['cz']

        eps = e**(-t_idle/t_eff)*tota_gate_fid

        n_cz = 0

        for i in full_code:
            if 'Rydberg' in i['name']:
                n_cz += 1

        results.loc[len(results)] = [variables, qaoa_depth, circuit.count_ops()['u3'], n_cz, compile_time, total_execution_time, eps]

    if not os.path.isfile('results/dpqa_results.csv'):
        results.to_csv('results/dpqa_results.csv')
    else:
        results.to_csv('results/dpqa_results.csv', index=False, mode='a', header=False)
