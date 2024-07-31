#from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit.providers.fake_provider import FakeWashingtonV2, FakeWashington
import pdb
#from utils.utils_fid import calculate_fidelity, estimate_fidelity
#from utils.quasi_distr import QuasiDistr
from time import perf_counter
import numpy as np
#import mapomatic.circuits as mm
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import gridspec
from weaver.utils.hamiltonians import Max3satHamiltonian
from weaver.utils.sat_utils import uniformly_random_independent_clauses
from weaver.utils.qaoa import QAOA
from qiskit import QuantumCircuit
from pysat.formula import CNF
from weaver.utils.circuit_utils import calculate_expected_fidelity
import pickle
from geyser.code.map_circuit import MapCircuit
from geyser.code.block_circuit import BlockCircuit
from geyser.code.compose_circuit import ComposeCircuit
from qiskit.dagcircuit import DAGCircuit, DAGOpNode
from evaluation.utils.gate_length_estimator import GateLengthEstimator
from qiskit.converters import circuit_to_dag
from evaluation.utils.utils_fid import calculate_expected_fidelity

gate_time_1q = 5.0e-07
gate_time_1qplus = 2.0e-07

def compute_execution_time(circuit):
    dag = circuit_to_dag(circuit)

    path = dag.longest_path()

    total_time = 0
    for i in path:
        if isinstance(i, DAGOpNode):
            if i.name == 'u3':
                total_time += gate_time_1q
            else:
                total_time += gate_time_1qplus
    return total_time

def run(config):
    basis_gates = ["rx", "rz", "x", "y", "z", "h", "id", "cz"]
    qaoa_depth = int(config['qaoa_depth'])
    instance_type = config['instance_type']
    qaoas_instances = []
    backend = FakeWashingtonV2()

    transpiled_circuits = []

    if instance_type == 'generated':
        instance_clauses = config['instance_clauses']

        if not isinstance(instance_clauses, list):
            instance_clauses = [instance_clauses]

        for clauses in instance_clauses:
            tmp = uniformly_random_independent_clauses(clauses)
            formula = CNF(from_clauses=tmp)
            tmp = Max3satHamiltonian(formula=formula)
            tmp = QAOA(tmp).naive_qaoa_circuit(qaoa_depth)
            qaoas_instances.append(tmp)

    else: #instance_type == "stored"
        instances_names = config['instances_names']
        
        if not isinstance(instances_names, list):
            instances_names = [instances_names]

        for file_name in instances_names:
            tmp_hamiltonion = Max3satHamiltonian('weaver/benchmarks/'+file_name)
            tmp_qaoa = QAOA(tmp_hamiltonion)#.naive_qaoa_circuit(qaoa_depth)
            qaoa_circuit, cost_params, mixer_params = tmp_qaoa.naive_qaoa_circuit(qaoa_depth)
            qaoas_instances.append([qaoa_circuit, cost_params, mixer_params])

    for qaoa_circuit, cost_params, mixer_params in qaoas_instances:
            bound_circuit = qaoa_circuit.assign_parameters({cost_params: [np.pi / 2.123 for param in cost_params], mixer_params: [np.pi / 3.123 for param in mixer_params]})
            bound_circuit.measure_all()
            transpiled_circuits.append(transpile(bound_circuit, basis_gates=basis_gates, optimization_level=3))
    
    results = pd.DataFrame(columns=['instance_type', 'instance_info', 'qaoa_depth', 'runtime', 'execution_time', 'eps'])
    
    basis_gates = ["u3", "id", "cz", "ccz", "cccz"]

    for circuit, instance_info in zip(transpiled_circuits, instance_clauses if instance_type == 'generated' else instances_names):
        print(f"Transpiling circuit {instance_info}")
        tmp = perf_counter()
        circuit = transpile(circuit, optimization_level=3, backend=backend)
        tmp = perf_counter()-tmp
        exec_time = GateLengthEstimator().estimate_circuit_execution_time(circuit, FakeWashington())

        eps = calculate_expected_fidelity(circuit, backend)

        #exec_time = compute_execution_time(circuit)
        results.loc[len(results)] = [instance_type, instance_info, qaoa_depth, tmp, exec_time, eps]
    
    results.to_csv('./evaluation/results/superconducting_results.csv')
    
def plot(config):
    pass