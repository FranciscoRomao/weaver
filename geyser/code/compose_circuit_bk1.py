import numpy as np

import multiprocessing
import qiskit.quantum_info as qi
from qiskit_aer import Aer
from qiskit import QuantumCircuit
from qiskit.compiler import transpile
from qiskit.converters import circuit_to_dag
from qiskit.dagcircuit import DAGOpNode

from scipy.optimize import dual_annealing

class ComposeCircuit:

	def __init__(self, algo, layout, circuit):
		self.algo = algo

		self.num_qubits = circuit.num_qubits

		self.layout = layout

		self.gates = {}

		cz = QuantumCircuit(2, name='cz')

		cz.cz(0, 1)

		self.gates[2] = cz.to_instruction()

		ccz = QuantumCircuit(3, name='ccz')

		ccz.h(2)
		ccz.ccx(0, 1, 2)
		ccz.h(2)

		self.gates[3] = ccz.to_instruction()

		cccz = QuantumCircuit(4, name='cccz')

		cccz.cu1(np.pi/4, 0, 3)
		cccz.cx(0, 1)
		
		cccz.cu1(-np.pi/4, 1, 3)
		cccz.cx(0, 1)

		cccz.cu1(np.pi/4, 1, 3)
		cccz.cx(1, 2)
		
		cccz.cu1(-np.pi/4, 2, 3)
		cccz.cx(0, 2)

		cccz.cu1(np.pi/4, 2, 3)
		cccz.cx(1, 2)
		
		cccz.cu1(-np.pi/4, 2, 3)
		cccz.cx(0, 2)

		cccz.cu1(np.pi/4, 2, 3)

		self.gates[4] = cccz.to_instruction()

		self.confs = {}
		self.confs[2] = [[0, 1], [1, 0]]
		self.confs[3] = [[1, 2, 0], [0, 2, 1], [0, 1, 2]]
		self.confs[4] = [[1, 2, 3, 0], [0, 2, 3, 1], [0, 1, 3, 2], [0, 1, 2, 3]]

		self.pulses = {'u3':1, 'cz':3, 'ccz':5, 'cccz':7}

		self.circuit = self.generate_composed_circuit(circuit)

	def get_circuit_pulses(self, circuit):
		dag = circuit_to_dag(circuit)

		total_depth = 0
		num_pulses = 0

		for l_id, layer in enumerate(list(dag.multigraph_layers())):

			depth = 0
			for node in layer:
				if isinstance(node, DAGOpNode):
					if node.name:
						depth = max(depth, self.pulses[node.name])
						num_pulses += self.pulses[node.name]
			total_depth += depth

		return num_pulses

	def hs_distance(self, A, B):
		return np.abs(1 - np.abs(np.sum(np.multiply(A,np.conj(B)))) / A.shape[0])

	'''
	def score(self, x, block_num_qubits, block_ideal_unitary):
		circuit = QuantumCircuit(block_num_qubits)

		index = 0
		while index < len(x):

			for qubit in range(block_num_qubits):
				circuit.u3(x[index], x[index+1], x[index+2], qubit)
				index += 3

			if index < len(x) and block_num_qubits > 1:
				conf = max(min(int(x[index]), block_num_qubits-1), 0)
				circuit.append(self.gates[block_num_qubits], self.confs[block_num_qubits][conf])
				index += 1

		#real_unitary = Aer.get_backend('unitary_simulator').execute(circuit).result().get_unitary(circuit)
		real_unitary = execute(circuit, Aer.get_backend('unitary_simulator')).result().get_unitary(circuit)

		distance = self.hs_distance(block_ideal_unitary, real_unitary)

		return distance
	'''
	
	def score(self, x, block_num_qubits, block_ideal_unitary):
		circuit = QuantumCircuit(block_num_qubits)
		
		index = 0
		while index < len(x):
			for qubit in range(block_num_qubits):
				circuit.u3(x[index], x[index + 1], x[index + 2], qubit)
				index += 3

			if index < len(x) and block_num_qubits > 1:
				conf = max(min(int(x[index]), block_num_qubits - 1), 0)
				circuit.append(
                    self.gates[block_num_qubits], self.confs[block_num_qubits][conf]
                )
				index += 1

		real_unitary = qi.Operator(circuit).data

        # real_unitary = execute(circuit, Aer.get_backend('unitary_simulator')).result().get_unitary(circuit)

		distance = self.hs_distance(block_ideal_unitary, real_unitary)

		return distance


	def compose_block(self, block):
		ret_block = None
		original_pulses = 0
		dag = circuit_to_dag(block)
		for l_id, layer in enumerate(list(dag.multigraph_layers())):
			for node in layer:
				if isinstance(node, DAGOpNode):
					if node.name:
						original_pulses = self.get_circuit_pulses(node.op._definition)
						ret_block = node.op._definition
						ret_block.name = block.name

		#block_ideal_unitary = execute(block, Aer.get_backend('unitary_simulator')).result().get_unitary(block)
		block_ideal_unitary = Aer.get_backend('unitary_simulator').execute(block).result().get_unitary(block)

		bounds = []
		comp_pulses = 0
		bounds += [(0, 2*np.pi) for _ in range(3*block.num_qubits)]
		comp_pulses += block.num_qubits

		distance = 1
		params = None

		while distance > 1e-1:

			if block.num_qubits > 1:
				bounds += [(0, block.num_qubits-1e-5)]
				comp_pulses += block.num_qubits * 2 - 1
			bounds += [(0, 2*np.pi) for _ in range(3*block.num_qubits)]
			comp_pulses += block.num_qubits

			if comp_pulses > original_pulses:
				return ret_block

			res = dual_annealing(self.score,
								 bounds=bounds,
								 args=(block.num_qubits, block_ideal_unitary),
								 initial_temp=5.e4,
								 minimizer_kwargs={'method':'L-BFGS-B', 'options':{'maxfun':1e4, 'eps':1e-6}},
								 restart_temp_ratio=5e-5,
								 maxfun=1e8)

			if res.fun < distance:
				distance = res.fun
				params = res.x

		index = 0
		comp_block = QuantumCircuit(block.num_qubits, name=block.name)

		while index < len(params):

			for qubit in range(comp_block.num_qubits):
				comp_block.u3(params[index], params[index+1], params[index+2], qubit)
				index += 3

			if index < len(params) and block.num_qubits > 1:
				conf = max(min(int(params[index]), block.num_qubits-1), 0)
				comp_block.append(self.gates[block.num_qubits], self.confs[block.num_qubits][conf])
				index += 1

		return comp_block

	def generate_composed_circuit(self, circuit):
		pool = multiprocessing.Pool()

		dag = circuit_to_dag(circuit)

		qubit_evo = [[] for _ in range(self.num_qubits)]

		original_blocks = []
		original_qubits = []

		for l_id, layer in enumerate(list(dag.multigraph_layers())):
			for node in layer:
				if isinstance(node, DAGOpNode):
					if node.name:
						qubits = [node.qargs[i].index for i in range(len(node.qargs))]
						original_qubits.append(qubits)

						block = QuantumCircuit(len(qubits), name=node.name)
						block.append(node.op, list(range(len(qubits))))
						original_blocks.append(block)

		composed_blocks = pool.map(self.compose_block, original_blocks)

		composed_circuit = QuantumCircuit(self.num_qubits)
		for qubits, block in zip(original_qubits, composed_blocks):
				composed_block = block.to_instruction()
				composed_circuit.append(composed_block, qubits)
		return composed_circuit

	def get_composed_circuit(self):
		return self.circuit
