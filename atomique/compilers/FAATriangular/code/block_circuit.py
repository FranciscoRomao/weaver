# import multiprocessing

from qiskit import QuantumCircuit
from qiskit.converters import circuit_to_dag


class BlockCircuit:

    def __init__(self, layout, blocks, circuit):

        self.num_qubits = circuit.num_qubits

        self.layout = layout

        self.blocks = blocks

        dag = circuit_to_dag(circuit)

        self.qubit_evo = [[] for _ in range(self.num_qubits)]
        for l_id, layer in enumerate(list(dag.multigraph_layers())):
            for node in layer:
                if node.__slots__[0] == "wire":
                    continue
                if node.name == "u3":
                    q = node.qargs[0].index
                    self.qubit_evo[q].append([l_id, node.name, node.op])
                elif node.name == "cz":
                    q1 = node.qargs[0].index
                    q2 = node.qargs[1].index
                    self.qubit_evo[q1].append([l_id, node.name, node.op, q2, "control"])
                    self.qubit_evo[q2].append([l_id, node.name, node.op, q1, "target"])

        self.lengths = [len(self.qubit_evo[q]) for q in range(self.num_qubits)]

        self.frontier = [0] * self.num_qubits

        self.weights = {"u3": 0.1, "cz": 1}

        self.circuit = self.generate_blocked_circuit(circuit)

    def calculate_block_score(self, x):

        block = self.blocks[x]["qubits"]

        layer = [
            self.qubit_evo[q][self.frontier[q]][0]
            for q in block
            if self.frontier[q] < self.lengths[q]
        ]

        positions = {q: self.frontier[q] for q in block}

        if not layer:
            return 0, positions

        score = 0

        layer = min(layer)

        removed_qubits = [q for q in block if self.frontier[q] >= self.lengths[q]]

        while len(removed_qubits) < len(block):

            should_be_removed = []

            for q in block:

                if (
                    q not in removed_qubits
                    and self.qubit_evo[q][positions[q]][0] == layer
                ):

                    if len(self.qubit_evo[q][positions[q]]) == 5 and (
                        self.qubit_evo[q][positions[q]][3] not in block
                        or self.qubit_evo[q][positions[q]][3] in removed_qubits
                    ):
                        should_be_removed.append(q)
                    else:
                        score += self.weights[self.qubit_evo[q][positions[q]][1]]
                        positions[q] += 1
                        if positions[q] == self.lengths[q]:
                            should_be_removed.append(q)

            for q in should_be_removed:
                removed_qubits.append(q)

            layer += 1

        return score, positions

    def get_best_schedule(self, this_block, excluded_blocks, schedule, total_score):

        if not self.blocks[this_block]["compatibles"] or all(
            [t in excluded_blocks for t in self.blocks[this_block]["compatibles"]]
        ):
            return total_score + self.block_scores[this_block], schedule + [this_block]

        sched = [t for t in schedule] + [this_block]

        total_score += self.block_scores[this_block]

        excl_blocks = [t for t in excluded_blocks] + [this_block]
        excl_blocks += self.blocks[this_block]["exclusions_l1"]
        excl_blocks += self.blocks[this_block]["exclusions_l2"]

        best_score = total_score
        best_schedule = sched
        for t in self.blocks[this_block]["compatibles"]:
            if t not in excluded_blocks:
                score, schedule = self.get_best_schedule(
                    t, excl_blocks + [t], sched, total_score
                )
                if score > best_score:
                    best_score = score
                    best_schedule = schedule

        return best_score, best_schedule

    def get_start_block_schedule(self, block):

        return self.get_best_schedule(block, [], [], 0)

    def generate_blocked_circuit(self, circuit):

        cycle = 0

        final_blocks = []

        # pool = multiprocessing.Pool()

        while self.frontier != self.lengths:

            output = []
            for key in self.blocks.keys():
                output.append(self.calculate_block_score(key))
            # output = pool.map(self.calculate_block_score, self.blocks.keys())

            self.block_scores = [o[0] for o in output]
            block_positions = [o[1] for o in output]

            output = []
            for key in self.blocks.keys():
                output.append(self.get_start_block_schedule(key))
            # output = pool.map(self.get_start_block_schedule, self.blocks.keys())

            best_score = 0
            best_schedule = None
            for o in output:
                if o[0] > best_score:
                    best_score = o[0]
                    best_schedule = o[1]

            for block in best_schedule:

                positions = {}

                for q in self.blocks[block]["qubits"]:

                    for p in range(self.frontier[q], block_positions[block][q]):

                        if self.qubit_evo[q][p][0] not in positions:
                            positions[self.qubit_evo[q][p][0]] = []

                        if self.qubit_evo[q][p][1] == "u3":
                            positions[self.qubit_evo[q][p][0]].append(
                                [self.qubit_evo[q][p][2], q]
                            )
                        elif self.qubit_evo[q][p][4] == "control":
                            positions[self.qubit_evo[q][p][0]].append(
                                [self.qubit_evo[q][p][2], q, self.qubit_evo[q][p][3]]
                            )
                        else:
                            assert self.qubit_evo[q][p][4] == "target"

                    self.frontier[q] = block_positions[block][q]

                if positions:

                    final_blocks.append(
                        ["c" + str(cycle) + "b" + str(block), positions]
                    )

            cycle += 1

        blocked_circuit = QuantumCircuit(self.num_qubits)

        for block in final_blocks:

            layers = sorted(list(block[1].keys()))

            qubits = []

            for layer in layers:

                for op in block[1][layer]:

                    qubits.append(op[1])

                    if len(op) == 3:
                        qubits.append(op[2])

            qubits = sorted(list(set(qubits)))

            cir = QuantumCircuit(len(qubits), name=block[0])

            for layer in layers:

                for op in block[1][layer]:

                    if len(op) == 2:
                        cir.append(op[0], [qubits.index(op[1])])
                    else:
                        cir.append(op[0], [qubits.index(op[1]), qubits.index(op[2])])

            cir = cir.to_instruction()

            blocked_circuit.append(cir, qubits)

        return len(final_blocks), blocked_circuit

    def get_blocked_circuit(self):

        return self.circuit
