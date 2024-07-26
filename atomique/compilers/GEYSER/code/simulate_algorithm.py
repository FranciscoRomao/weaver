import logging

logging.disable(logging.INFO)
import multiprocessing

import numpy as np
import pdb
# import qiskit.quantum_info as qi
from block_circuit import BlockCircuit
from compose_circuit import ComposeCircuit
from map_circuit import MapCircuit
from qiskit import Aer, QuantumCircuit, execute, transpile

ALGORITHMS = [
    "bv_n50",
    #"bv_n70",
    #"hhl_n7",
    #"QV_n32",
    #"supermarq_mermin_bell_n10",
]

NUM_ITERATIONS = 1

def hs_distance(A, B):
    return np.sqrt(
        np.abs(1 - (np.abs(np.sum(np.multiply(A, np.conj(B)))) / A.shape[0]) ** 2)
    )


def main():
    #pdb.set_trace()
    for i in range(len(ALGORITHMS)):
        algo = ALGORITHMS[i]

        print(algo.upper())

        algo_file = "../qasm/" + algo + "_original.qasm"

        circuits = {}

        circuits["Original"] = QuantumCircuit.from_qasm_file(algo_file)

        layout = None
        blocks = None
        min_num_blocks = float("inf")

        for _ in range(NUM_ITERATIONS):
            mapper = MapCircuit(circuits["Original"])

            layout = mapper.get_layout()

            blocks = mapper.get_blocks()

            mapped = mapper.get_mapped_circuit()

            blocker = BlockCircuit(layout, blocks, mapped)

            num_blocks, blocked = blocker.get_blocked_circuit()

            if num_blocks < min_num_blocks:
                circuits["Mapped"] = mapped
                circuits["Blocked"] = blocked
                min_num_blocks = num_blocks

        with open("../qasm/" + algo + "_mapped.qasm", "w") as f:
            f.write(circuits["Mapped"].qasm())

        print("Circuit Mapped")

        with open("../qasm/" + algo + "_blocked.qasm", "w") as f:
            f.write(circuits["Blocked"].qasm())

        print("Circuit Blocked")

        composer = ComposeCircuit(algo, layout, circuits["Blocked"])
        circuits["Composed"] = composer.get_composed_circuit()

        with open("../qasm/" + algo + "_composed.qasm", "w") as f:
            f.write(circuits["Composed"].qasm())

        print("Circuit Composed")
        #pdb.set_trace()
        n_pulse = composer.get_n_pulses()
        print("Number of pulses:", n_pulse)
        with open("../qasm/" + algo + "_result.txt", "w") as f:
            f.write("Number of pulses: " + str(n_pulse))


if __name__ == "__main__":
    main()
