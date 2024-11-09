#%%
from catalyst import qjit, measure, cond, for_loop, while_loop
import pennylane as qml
from jax import numpy as jnp
from jax.core import ShapedArray
import jax
from jax import grad, jit, vmap
import optax
#from __future__ import annotations
import cirq
from qiskit.quantum_info import hellinger_fidelity
from supermarq.benchmark import Benchmark

#%%
#dev = qml.device("lightning.qubit", wires=20)


class GHZ(Benchmark):
    def __init__(self, num_qubits: int) -> None:
        """Initialize a `GHZ` object.

        Args:
            num_qubits: Number of qubits in GHZ circuit.
        """
        self.num_qubits = num_qubits

    def circuit(self) -> cirq.Circuit:
        """Generate an n-qubit GHZ circuit.

        Returns:
            A `cirq.Circuit`.
        """
        qubits = cirq.LineQubit.range(self.num_qubits)
        circuit = cirq.Circuit()
        circuit.append(cirq.H(qubits[0]))
        for i in range(self.num_qubits - 1):
            circuit.append(cirq.CNOT(qubits[i], qubits[i + 1]))
        circuit.append(cirq.measure(*qubits))
        return circuit

    def score(self, counts: dict[str, int]) -> float:
        r"""Compute the Hellinger fidelity between the experimental and ideal results.

        The ideal results are 50% probabilty of measuring the all-zero state and 50% probability
        of measuring the all-one state.

        The formula for the Hellinger fidelity between two distributions p and q is given by
        $(\sum_i{p_i q_i})^2$.

        Args:
            counts: A dictionary containing the measurement counts from circuit execution.

        Returns:
            Hellinger fidelity as a float.
        """
        # Create an equal weighted distribution between the all-0 and all-1 states
        ideal_dist = {b * self.num_qubits: 0.5 for b in ["0", "1"]}
        total_shots = sum(counts.values())
        device_dist = {bitstr: count / total_shots for bitstr, count in counts.items()}
        return hellinger_fidelity(ideal_dist, device_dist)

#ghz_size = 10
#
#@for_loop(1, ghz_size, 1)
#def cnot_loop(i, *args):
#    qml.CNOT([i, i+1])
#
#
#@qml.qnode(dev)
#def circuit(ghz_size: jnp.int64):
#
#    qml.Hadamard(0)
#    
#    for i in range(ghz_size):
#        cnot_loop(i)
#
#    measurements = [qml.expval(qml.PauliZ(0))]
#    for i in range(1,ghz_size):
#        measurements.append(qml.expval(qml.PauliZ(i+1)))
#
#    return measurements
##%%
#
#res = circuit(5)
#
##%%
#
#circuit(10)
#
#
##%%
#
#circuit(15)
#
##%%
#circuit(20)