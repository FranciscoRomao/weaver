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
from geyser.code.map_circuit import MapCircuit
from geyser.code.block_circuit import BlockCircuit
from geyser.code.compose_circuit import ComposeCircuit

def run_geyser(circuit, iterations):
    layout = None
    blocks = None
    min_num_blocks = float('inf')

    circuits = {}
    circuits['Original'] = circuit
    
    for i in range(iterations):
        print(f"Geyser mapping and blocking iteration {i+1}")
        mapper = MapCircuit(circuits['Original'])
        layout = mapper.get_layout()
        blocks = mapper.get_blocks()
        mapped = mapper.get_mapped_circuit()
        blocker = BlockCircuit(layout, blocks, mapped)
        num_blocks, blocked = blocker.get_blocked_circuit()

        if num_blocks < min_num_blocks:
            circuits['Mapped'] = mapped
            circuits['Blocked'] = blocked
            min_num_blocks = num_blocks

    composer = ComposeCircuit("blabla", layout, circuits['Blocked'])    
    print("Circuit composed.")
    return composer.get_composed_circuit()

def run_fpqac(circuit, iterations):
    pass

def run(config):

    basis_gates = ["rx", "rz", "x", "y", "z", "h", "id", "cz"]
    qaoa_depth = int(config['qaoa_depth'])
    geyset_iterations = int(config['iterations'])
    instance_type = config['instante_type']
    qaoas_instances = []

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

    else: #instance_type == "stored"
        instances_names = config['instances_names']
        
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

    pdb.set
    
    results = pd.DataFrame(columns=['instance_type', 'instance_info', 'qaoa_depth', 'geyser_iterations', 'runtime', 'optimized_circuit'])
    
    for circuit, instance_info in zip(transpiled_circuits, instance_clauses if instance_type == 'generated' else instances_names):
        tmp = perf_counter()
        geyser_opt_circuit = run_geyser(circuit, geyset_iterations)
        tmp = perf_counter()-tmp
        results.loc[len(results)] = [instance_type, instance_info, qaoa_depth, geyset_iterations, tmp, pickle.dumps(geyser_opt_circuit.qasm())]
        results.to_csv('./evaluation/results/geyser_results.csv', mode='a', header=False, index=False)
        results = results[:-1]

    
def plot(config):
    pass