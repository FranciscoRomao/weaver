import os
import pdb
import random

import numpy as np
from qiskit import QuantumCircuit

pdb.set_trace()


def gen_random_circuit(n_qubits, n_2q_gate, max_distance_2q, n_interact_q, n_circ):
    os.makedirs(
        f"q{n_qubits}/ng{n_2q_gate}/maxd{max_distance_2q}_ninter{n_interact_q}",
        exist_ok=True,
    )

    for i in range(n_circ):
        circ = QuantumCircuit(n_qubits)
        n_2q_gate_qubit_dict = {}
        interact_qubit_dict = {}
        for k in range(n_qubits):
            n_2q_gate_qubit_dict[k] = 0
            interact_qubit_dict[k] = set()
        gate_pair_list = []
        while True:
            # get index of qubits that still need to be added gates:
            q0_candidates = [
                q for q in range(n_qubits) if n_2q_gate_qubit_dict[q] < n_2q_gate
            ]
            if (
                len(q0_candidates) < 2
                or len(gate_pair_list) >= n_2q_gate * n_qubits // 2
            ):
                break
            q0 = random.choice(q0_candidates)
            if len(interact_qubit_dict[q0]) >= n_interact_q:
                q1 = random.choice(list(interact_qubit_dict[q0]))
            else:
                if max_distance_2q == 999:
                    q1 = (q0 + random.randint(1, n_qubits)) % n_qubits
                else:
                    q1 = (q0 + random.randint(1, max_distance_2q)) % n_qubits

                if q1 == q0:
                    q1 = (q0 + 1) % n_qubits
            interact_qubit_dict[q0].add(q1)
            interact_qubit_dict[q1].add(q0)
            n_2q_gate_qubit_dict[q0] += 1
            n_2q_gate_qubit_dict[q1] += 1
            gate_pair_list.append([q0, q1])

        #     gate_pair_list = []
        #     for q0 in range(n_qubits):
        #         # choose n_interact_q distances
        #         q0_q1_distance_candidates = random.sample(range(1, max_distance_2q + 1), k=int(np.ceil(n_interact_q/2)))
        #         q0_q1_distances = random.choices(q0_q1_distance_candidates, k=int(np.ceil(n_2q_gate/2)))
        #         for dis in q0_q1_distances:
        #             gate_pair_list.append((q0, (q0 + dis) % n_qubits))

        random.shuffle(gate_pair_list)
        for q0, q1 in gate_pair_list:
            circ.cx(q0, q1)
            circ.rx(random.random(), q0)
            circ.ry(random.random(), q1)

        print(
            f"overall n gates: {len(gate_pair_list)}, n 2q gates: {n_2q_gate}, n_interact_q: {n_interact_q}"
        )
        print(n_2q_gate_qubit_dict)
        print(interact_qubit_dict)

        # for _ in range(n_2q_gate * n_qubits):
        #     qubit_1 = random.randint(0, n_qubits - 1)
        #     qubit_2 = (qubit_1 + random.randint(1, distance_2q)) % n_qubits
        #     # qubit_2 = (qubit_1 + distance_2q) % n_qubits
        #     if qubit_1 == qubit_2:
        #         qubit_2 = (qubit_1 + 1) % n_qubits
        #     circ.cz(qubit_1, qubit_2)
        #     circ.rx(random.random(), qubit_1)
        #     circ.ry(random.random(), qubit_2)

        with open(
            f"q{n_qubits}/ng{n_2q_gate}/maxd{max_distance_2q}_ninter{n_interact_q}/i{i}.qasm",
            "w",
        ) as f:
            f.write(circ.qasm())
    return circ


if __name__ == "__main__":
    for n_qubits in [70]:
        for n_2q_gates in [2, 6, 10, 14, 18, 22, 26]:
            for dist in [10]:
                for n_inter in range(1, 8):
                    gen_random_circuit(
                        n_qubits=n_qubits,
                        n_2q_gate=n_2q_gates,
                        max_distance_2q=dist,
                        n_interact_q=n_inter,
                        n_circ=10,
                    )
