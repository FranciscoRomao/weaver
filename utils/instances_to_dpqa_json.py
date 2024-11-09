from qiskit import transpile
import pdb
from time import perf_counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
from compilers.weaver.utils.hamiltonians import Max3satHamiltonian
from compilers.weaver.utils.sat_utils import uniformly_random_independent_clauses
from compilers.weaver.utils.qaoa import QAOA
from qiskit import QuantumCircuit
from compilers.weaver.utils.circuit_utils import calculate_expected_fidelity
import pickle
from pysat.formula import CNF
import json
import os

instances_names = ['uf20-09.cnf',
                    'uf20-010.cnf']
qaoa_depth = 1

def run():

    basis_gates = ["u3", "cz"]
    qaoas_instances = []
    transpiled_circuits = []
    
    #if not isinstance(instances_names, list):
    #    instances_names = [instances_names]
#
    #for file_name in instances_names:
    #    tmp_hamiltonion = Max3satHamiltonian('benchmarks/max3SAT/'+file_name)
    #    tmp_qaoa = QAOA(tmp_hamiltonion)#.naive_qaoa_circuit(qaoa_depth)
    #    qaoa_circuit, cost_params, mixer_params = tmp_qaoa.naive_qaoa_circuit(qaoa_depth)
    #    qaoas_instances.append([qaoa_circuit, cost_params, mixer_params])
#
    #for i, qaoas_instance in enumerate(qaoas_instances):
    #    qaoa_circuit, cost_params, mixer_params = qaoas_instance
    #    print(f"Transpiling circuit {i} out of {len(qaoas_instances)}")
    #    bound_circuit = qaoa_circuit.assign_parameters({cost_params: [np.pi / 2.123 for param in cost_params], mixer_params: [np.pi / 3.123 for param in mixer_params]})
    #    bound_circuit.measure_all()
    #    transpiled_circuits.append(transpile(bound_circuit, basis_gates=basis_gates, optimization_level=3))

    cz_gates = []

    #for i, circuit in enumerate(transpiled_circuits):
    #    if os.path.exists('benchmarks/DPQA/' + instances_names[i].replace('.cnf', '.qasm')):
    #        continue
    #    with open('benchmarks/DPQA/' + instances_names[i].replace('.cnf', '.qasm'), 'x') as f:
    #        f.write(circuit.qasm())

    for name in instances_names:
        with open('benchmarks/QASMBench/' + name.replace('.cnf', '.qasm'), 'r') as f:
            qasm = f.read()
            transpiled_circuits.append(QuantumCircuit.from_qasm_str(qasm))
    

    for i,circuit in enumerate(transpiled_circuits):
        cz_gates.append([])
        for instr in circuit.data:
            if instr[0].name == 'cz':
                cz_gates[i].append([instr[1][0].index, instr[1][1].index])

    n_variables = [transpiled_circuits[i].num_qubits for i in range(len(transpiled_circuits))]
    
    transformed_list = {}
    for i in range(len(transpiled_circuits)):
        transformed_list[str(n_variables[i])] = [[]]
    

    for i in range(len(transpiled_circuits)):
        n_variant = instances_names[i].split('-')[1].strip('.cnf')
        for cz in cz_gates[i]:
            #check if the last one added is not the same
            if transformed_list[str(n_variables[i])][0] == []:
                transformed_list[str(n_variables[i])][0].append([cz[0], cz[1]])
            elif transformed_list[str(n_variables[i])][0][-1] != [cz[0], cz[1]]:
                transformed_list[str(n_variables[i])][0].append([cz[0], cz[1]])

        with open(f"benchmarks/DPQA/graph{n_variables[i]}_{n_variant}.json", "w") as outfile:
            json.dump(transformed_list, outfile, indent=4)

    #for circuit, name in zip(transpiled_circuits, instance_clauses if instance_type == 'generated' else instances_names):
    #    if instance_type == 'generated':
    #        name = 'generated_' + str(qaoa_depth) + 'n' + str(name)
    #    with open('./evaluation/benchmarks/QASMBench/' + name + '.qasm', 'w') as f:
    #        f.write(circuit.qasm())