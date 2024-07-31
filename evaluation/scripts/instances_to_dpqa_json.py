from qiskit import transpile
import pdb
from time import perf_counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
from weaver.utils.hamiltonians import Max3satHamiltonian
from weaver.utils.sat_utils import uniformly_random_independent_clauses
from weaver.utils.qaoa import QAOA
from qiskit import QuantumCircuit
from weaver.utils.circuit_utils import calculate_expected_fidelity
import pickle
import json

def run(config):

    basis_gates = ["u3", "cz"]
    qaoa_depth = int(config['qaoa_depth'])
    instances_names = config['instances_names']
    qaoas_instances = []
    instance_type = config['instance_type']

    transpiled_circuits = []
    
    if instance_type == 'generated':
        instance_clauses = config['instance_clauses']

        if not isinstance(instance_clauses, list):
            instance_clauses = [instance_clauses]

        for clauses in instance_clauses:
            tmp = uniformly_random_independent_clauses(clauses)
            tmp = Max3satHamiltonian(clauses=tmp)
            tmp = QAOA(tmp).naive_qaoa_circuit(qaoa_depth)
            qaoas_instances.append(tmp)
    else:
        if not isinstance(instances_names, list):
            instances_names = [instances_names]

        for file_name in instances_names:
            tmp_hamiltonion = Max3satHamiltonian('weaver/benchmarks/'+file_name)
            tmp_qaoa = QAOA(tmp_hamiltonion)#.naive_qaoa_circuit(qaoa_depth)
            qaoa_circuit, cost_params, mixer_params = tmp_qaoa.naive_qaoa_circuit(qaoa_depth)
            qaoas_instances.append([qaoa_circuit, cost_params, mixer_params])

    for i, qaoas_instance in enumerate(qaoas_instances):
        qaoa_circuit, cost_params, mixer_params = qaoas_instance
        print(f"Transpiling circuit {i} out of {len(qaoas_instances)}")
        bound_circuit = qaoa_circuit.assign_parameters({cost_params: [np.pi / 2.123 for param in cost_params], mixer_params: [np.pi / 3.123 for param in mixer_params]})
        bound_circuit.measure_all()
        transpiled_circuits.append(transpile(bound_circuit, basis_gates=basis_gates, optimization_level=3))


    cz_gates = []

    for circuit in transpiled_circuits:
        for instr in circuit.data:
            if instr[0].name == 'cz':
                cz_gates.append([instr[1][0].index, instr[1][1].index])

    pdb.set_trace()
    transformed_list = {"111": [[]]}

    for cz in cz_gates:
        #check if the last one added is not the same
        if transformed_list["111"][0] == []:
            transformed_list["111"][0].append([cz[0], cz[1]])
        elif transformed_list["111"][0][-1] != [cz[0], cz[1]]:
            transformed_list["111"][0].append([cz[0], cz[1]])

    with open("output.json", "w") as outfile:
        json.dump(transformed_list, outfile, indent=4)

    #for circuit, name in zip(transpiled_circuits, instance_clauses if instance_type == 'generated' else instances_names):
    #    if instance_type == 'generated':
    #        name = 'generated_' + str(qaoa_depth) + 'n' + str(name)
    #    with open('./evaluation/benchmarks/QASMBench/' + name + '.qasm', 'w') as f:
    #        f.write(circuit.qasm())
    
def plot(config):
    pass