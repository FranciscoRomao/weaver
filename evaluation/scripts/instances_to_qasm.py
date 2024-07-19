#from qiskit import QuantumCircuit
from qiskit import transpile
#from qiskit_ibm_runtime.fake_provider.backends import FakeWashington
#from qiskit.providers.fake_provider import FakeWashington, FakeKolkata
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
from fpqa_max3sat.utils.hamiltonians import Max3satHamiltonian
from fpqa_max3sat.utils.sat_utils import uniformly_random_independent_clauses
from fpqa_max3sat.utils.qaoa import QAOA
from qiskit import QuantumCircuit

from fpqa_max3sat.utils.circuit_utils import calculate_expected_fidelity
import pickle

def run(config):

    basis_gates = ["rx", "rz", "x", "y", "z", "h", "id", "cz"]
    qaoa_depth = int(config['qaoa_depth'])
    instances_names = config['instances_names']
    qaoas_instances = []

    transpiled_circuits = []
    
    if not isinstance(instances_names, list):
        instances_names = [instances_names]

    for file_name in instances_names:
        tmp_hamiltonion = Max3satHamiltonian('fpqa_max3sat/instances/'+file_name)
        tmp_qaoa = QAOA(tmp_hamiltonion)#.naive_qaoa_circuit(qaoa_depth)
        qaoa_circuit, cost_params, mixer_params = tmp_qaoa.naive_qaoa_circuit(qaoa_depth)
        qaoas_instances.append([qaoa_circuit, cost_params, mixer_params])

    for qaoa_circuit, cost_params, mixer_params in qaoas_instances:
        bound_circuit = qaoa_circuit.assign_parameters({cost_params: [np.pi / 2.123 for param in cost_params], mixer_params: [np.pi / 3.123 for param in mixer_params]})
        bound_circuit.measure_all()
        transpiled_circuits.append(transpile(bound_circuit, basis_gates=basis_gates, optimization_level=3))
        
    for circuit, name in zip(transpiled_circuits, instances_names):
        with open('./evaluation/benchmarks/QASMBench/' + name + '.qasm', 'w') as f:
            f.write(circuit.qasm())
    
def plot(config):
    pass