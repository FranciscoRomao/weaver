import pickle
from qiskit import QuantumCircuit
from qiskit import transpile
import pandas as pd
import pdb



data = pd.read_csv('evaluation/results/geyser_results.csv')

data = data.loc[36:44]


n_variables = [20, 50]
pdb.set_trace()
gates1q = []
gates2q = []
data.to_csv('evaluation/results/geyser_results_new.csv')
exit()
for vars in n_variables:

    circuit = data[data['n_variables']==vars]['optimized_circuit'].values

    combined_bytes = b''.join(bytes(item[2:-1], 'utf-8').decode('unicode_escape').encode('raw_unicode_escape') for item in circuit)

    circuit = pickle.loads(combined_bytes)

    circ = QuantumCircuit.from_qasm_str(circuit)

    transpiled_circ = transpile(circ, basis_gates=['u3', 'cz'], optimization_level=3)

    gates1q.append(transpiled_circ.count_ops()['u3'])

    gates2q.append(transpiled_circ.count_ops()['cz'])

data['gates1q'] = gates1q
data['gates2q'] = gates2q





##variants = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1', 'j1']
##
##sizes = [20, 50, 100, 150, 250]
##
### open qasm file to quantum circuit
##
##pdb.set_trace()
##
##for var in variants:
##    for size in sizes:
##        with open(f'evaluation/benchmarks/QASMBench/{var}_n{size}.qasm', 'r') as file:
##            circuit = file.read()
##
##        circ = QuantumCircuit.from_qasm_str(circuit)