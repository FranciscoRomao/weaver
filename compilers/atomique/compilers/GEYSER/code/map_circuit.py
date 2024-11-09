from qiskit.compiler import transpile


class MapCircuit:

    def __init__(self, circuit):

        self.num_qubits = circuit.num_qubits

        self.layout, self.qubit_conns, self.blocks = self.generate_qubit_map()

        self.circuit = transpile(
            circuit,
            basis_gates=["u3", "cz"],
            coupling_map=self.layout,
            optimization_level=3,
        )

    def generate_qubit_map(self):

        dimension_x = int(self.num_qubits**0.5)

        if dimension_x**2 != self.num_qubits:
            dimension_x += 1

        dimension_y = int(self.num_qubits / dimension_x)

        if dimension_x * dimension_y < self.num_qubits:
            dimension_y += 1

        layout = []
        qubit_conns = {}
        blocks = {}

        block_id = 0
        for row in range(dimension_y):
            for col in range(dimension_x):

                qubit_id = row * dimension_x + col

                if qubit_id == self.num_qubits:
                    break

                qubit_conns[qubit_id] = []

                conditions = [
                    col % dimension_x > 0,
                    row - 1 >= 0,
                    row - 1 >= 0 and col + 1 < dimension_x,
                    col + 1 < dimension_x
                    and row * dimension_x + col + 1 < self.num_qubits,
                    (row + 1) * dimension_x + col < self.num_qubits,
                    col % dimension_x > 0
                    and (row + 1) * dimension_x + col - 1 < self.num_qubits,
                ]

                qubits_ids = [
                    row * dimension_x + col - 1,
                    (row - 1) * dimension_x + col,
                    (row - 1) * dimension_x + col + 1,
                    row * dimension_x + col + 1,
                    (row + 1) * dimension_x + col,
                    (row + 1) * dimension_x + col - 1,
                ]

                for index, condition in enumerate(conditions):
                    if condition:
                        layout.append([qubit_id, qubits_ids[index]])
                        qubit_conns[qubit_id].append(qubits_ids[index])

                if conditions[3] and conditions[4]:
                    blocks[block_id] = {}
                    blocks[block_id]["qubits"] = [
                        qubit_id,
                        qubits_ids[3],
                        qubits_ids[4],
                    ]
                    block_id += 1
                if conditions[4] and conditions[5]:
                    blocks[block_id] = {}
                    blocks[block_id]["qubits"] = [
                        qubit_id,
                        qubits_ids[4],
                        qubits_ids[5],
                    ]
                    block_id += 1

        for t_1 in blocks.keys():

            blocks[t_1]["exclusions_l1"] = set()
            for t_2 in blocks.keys():
                if t_2 != t_1:
                    if any(
                        [
                            qubit in blocks[t_1]["qubits"]
                            for qubit in blocks[t_2]["qubits"]
                        ]
                    ):
                        blocks[t_1]["exclusions_l1"].add(t_2)

            blocks[t_1]["exclusions_l2"] = set()
            for t_2 in blocks.keys():
                if t_2 != t_1 and t_2 not in blocks[t_1]["exclusions_l1"]:
                    for t_3 in blocks[t_1]["exclusions_l1"]:
                        if any(
                            [
                                qubit in blocks[t_3]["qubits"]
                                for qubit in blocks[t_2]["qubits"]
                            ]
                        ):
                            blocks[t_1]["exclusions_l2"].add(t_2)

            blocks[t_1]["compatibles"] = set()
            for t_2 in blocks.keys():
                if (
                    t_2 != t_1
                    and t_2 not in blocks[t_1]["exclusions_l1"]
                    and t_2 not in blocks[t_1]["exclusions_l2"]
                ):
                    for t_3 in blocks[t_1]["exclusions_l2"]:
                        if any(
                            [
                                qubit in blocks[t_3]["qubits"]
                                for qubit in blocks[t_2]["qubits"]
                            ]
                        ):
                            blocks[t_1]["compatibles"].add(t_2)

        return layout, qubit_conns, blocks

    def get_layout(self):

        return self.layout

    def get_qubit_connections(self):

        return self.qubit_conns

    def get_blocks(self):

        return self.blocks

    def get_mapped_circuit(self):

        return self.circuit
