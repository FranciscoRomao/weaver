from time import time

import numpy as np
import yaml
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.random import random_circuit
from qiskit.converters import circuit_to_dag

from compilers.analyzer import Analyzer
from utils import Position, get_p2v_mapping, get_v2p_mapping, move_qubit_to_line


class HeuristicCompilerLogger(object):
    def __init__(self, circ, n_rows, n_cols, n_aods, backend_config):
        self.circ = circ
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_aods = n_aods
        self.backend_config = backend_config
        self.log = {"prop": {}, "code": []}

        self.n_X = n_cols
        self.n_Y = n_rows

        assert self.n_aods == 1

        self.n_current_ancilla = 0

        self.ancilla_occupation = {}

        self.ancilla_abs_pos_x = np.zeros((self.n_aods, self.n_X))
        self.ancilla_abs_pos_y = np.zeros((self.n_aods, self.n_Y))

        self.log["prop"]["slm_rel_pos"] = []

        num_qubits = self.circ.num_qubits
        for k in range(num_qubits):
            self.log["prop"]["slm_rel_pos"].append(
                Position(x=k % self.n_X, y=k // self.n_X, z=-1)
            )

        self.log["prop"]["max_ancilla"] = 1
        self.log["prop"]["n_qubits"] = num_qubits
        self.num_transfers = 0

    def new_code(self, type):
        self.log["code"].append({})
        code = self.log["code"][-1]
        code["data"] = []
        code["type"] = type
        # code["additional_args"] = {}
        return code

    def initialize_aod(self, aod_id_list):
        # move all lines to zero
        for aod_id in aod_id_list:
            for x in range(self.n_X):
                self.ancilla_abs_pos_x[aod_id][x] = x
            for y in range(self.n_Y):
                self.ancilla_abs_pos_y[aod_id][y] = y

    def prepare(self, qubit):
        code = self.new_code("prepare")
        aod_touched = {}
        # this is only one ancilla??
        self.n_current_ancilla = 1
        aod_touched[0] = True
        code["data"] = [
            {
                "slm_rel_pos": Position(x=qubit.x, y=qubit.y, z=-1),
                "ancilla_rel_pos": qubit,
            }
        ]

        self.initialize_aod(aod_touched.keys())

    def destroy(self, qubit):
        code = self.new_code("destroy")
        code["data"] = [{"ancilla_rel_pos": qubit}]

    def transfer(self, qubit):
        code = self.new_code("transfer")
        code["data"] = [{"source": qubit}]

    def qubitidx2Position(self, qubitidx):
        return Position(x=qubitidx % self.n_X, y=qubitidx // self.n_X, z=-1)

    def gate_2Q(self, my_list, additional_stage=0):
        # my_list=[(source_rel_pos: Position,target_rel_pos: Position)...]
        # self.log["prop"]["n_gate_2q"] += len(my_list)
        # self.log["prop"]["depth"] += 1
        code = self.new_code("gate_2Q")
        for item in my_list:
            code["data"].append({"source": item[0], "ancilla": item[1]})
        code["additional_stage"] = additional_stage

    def gate_1Q(self, my_list):
        # my_list=[source_rel_pos: Position...]
        code = self.new_code("gate_1Q")
        for item in my_list:
            code["data"].append({"source": item})

    def move_aod_to_aod(self, my_list):
        # my_list=[(new_target_rel_position: Position, ancilla_rel: Position)...]
        new_list = {i: [] for i in range(self.n_aods)}
        for item in my_list:
            if item[0].z > item[1].z:
                item[0], item[1] = item[1], item[0]
            new_list[item[1].z].append([item[0], item[1]])
        code = self.new_code("move")
        for i in range(self.n_aods):
            if len(new_list[i]) == 0:
                continue
            for item in new_list[i]:
                if item[0].z != -1:
                    item[0] = Position(
                        self.ancilla_abs_pos_x[item[0].z][item[0].x],
                        self.ancilla_abs_pos_y[item[0].z][item[0].y],
                        i,
                    )
            self.ancilla_abs_pos_x, self.ancilla_abs_pos_y = move_qubit_to_line(
                new_list[i],
                self.backend_config,
                self.ancilla_abs_pos_x,
                self.ancilla_abs_pos_y,
            )
        code["data"] = {
            "ancilla_abs_pos_x": self.ancilla_abs_pos_x.tolist(),
            "ancilla_abs_pos_y": self.ancilla_abs_pos_y.tolist(),
        }

    def get_log(self):
        num_1q_gates = 0
        num_2q_gates = 0
        num_layers_2 = 0
        num_layers_1 = 0

        dag = circuit_to_dag(self.circ)

        while True:
            add_layer_1 = False
            add_layer_2 = False
            front_layer = dag.front_layer()

            data_1q_source = []
            for node in front_layer:
                if node.op.num_qubits == 1:
                    dag.remove_op_node(node)
                    num_1q_gates += 1
                    add_layer_1 = True
                    data_1q_source.append(self.qubitidx2Position(node.qargs[0].index))

            if add_layer_1:
                self.gate_1Q(data_1q_source)

            if dag.depth() == 0:
                break

            gates_this_layer = []
            nodes_this_layer = []
            for node in front_layer:
                if node.op.num_qubits == 2:
                    nodes_this_layer.append(node)
                    gate_2q = list(map(lambda x: x.index, node.qargs))
                    if gate_2q[0] > gate_2q[1]:
                        gate_2q = [gate_2q[1], gate_2q[0]]
                    gates_this_layer.append(gate_2q)

            for gate_2q in gates_this_layer:
                q0, q1 = gate_2q
                q0_loc = self.qubitidx2Position(q0)
                q1_loc = self.qubitidx2Position(q1)
                # firstly transfer the slm to aod
                self.transfer(q0_loc)
                self.prepare(Position(x=q0_loc.x, y=q0_loc.y, z=0))
                self.move_aod_to_aod([[q1_loc, Position(x=q0_loc.x, y=q0_loc.y, z=0)]])
                self.gate_2Q([[q1_loc, Position(x=q0_loc.x, y=q0_loc.y, z=0)]])
                self.move_aod_to_aod([[q0_loc, Position(x=q0_loc.x, y=q0_loc.y, z=0)]])
                self.transfer(q0_loc)
                self.destroy(Position(x=q0_loc.x, y=q0_loc.y, z=0))
                self.num_transfers += 2

            for node in nodes_this_layer:
                dag.remove_op_node(node)
                num_2q_gates += 1
                add_layer_2 = True

            if add_layer_1:
                num_layers_1 += 1
            if add_layer_2:
                num_layers_2 += 1
            if dag.depth() == 0:
                break

        res = {
            "n_1q_gates": num_1q_gates,
            "n_2q_gates": num_2q_gates,
            "n_2q_layers": num_layers_2,
            "n_1q_layers": num_layers_1,
            "n_move": num_layers_2 - 1,
            "n_transfer": self.num_transfers,
        }

        return self.log

        # for inst in circ._data:
        #     op = inst.operation
        #     if op.name in ['u1', 'u2', 'u3', 'id']:
        #         num_1q_gates += 1
        #         info = {
        #             "data": [{"source": inst[1][0].index}],
        #             "type": "gate_1Q",
        #             "distance": 0,
        #         }
        #         code[str(code_id)] = info
        #         code_id += 1

        #     elif op.name == "cz":
        #         num_2q_gates += 1
        #         num_transfer += 2
        #         depth += 1

        #         # atom transfer:
        #         info = {
        #             "data": [{"source": inst[1][0].index}],
        #             "type": "transfer",
        #             "distance": 0,
        #         }
        #         code[str(code_id)] = info
        #         code_id += 1

        #         info = {
        #             "data": [{"source": inst[1][0].index}],
        #             "type": "create",
        #         }
        #         code[str(code_id)] = info
        #         code_id += 1

        #         # move to target:
        #         info = {
        #             "data": [{"source": inst[1][0].index, "target": inst[1][1].index}],
        #             "type": "move",
        #             "distance": grid_distance(
        #                 inst[1][0].index, inst[1][1].index, n_column=hyperparams.n_cols
        #             ),
        #         }
        #         code[str(code_id)] = info
        #         code_id += 1

        #         # 2q gate:
        #         info = {
        #             "data": [{"source": inst[1][0].index, "target": inst[1][1].index}],
        #             "type": "gate_2Q",
        #             "distance": 0,
        #         }
        #         code[str(code_id)] = info
        #         code_id += 1

        #         # move back to source:
        #         info = {
        #             "data": [{"source": inst[1][1].index, "target": inst[1][0].index}],
        #             "type": "move",
        #             "distance": grid_distance(
        #                 inst[1][0].index, inst[1][1].index, n_column=hyperparams.n_cols
        #             ),
        #         }
        #         code[str(code_id)] = info
        #         code_id += 1

        #         # atom transfer:
        #         info = {
        #             "data": [{"source": inst[1][0].index}],
        #             "type": "transfer",
        #             "distance": 0,
        #         }
        #         code[str(code_id)] = info
        #         code_id += 1

        #         # add destroy stage to reset the movement deltN
        #         info = {
        #             "data": [{"source": inst[1][0].index}],
        #             "type": "destroy",
        #             "distance": 0,
        #         }
        #         code[str(code_id)] = info
        #         code_id += 1

        # log["prop"]["gate_1q"] = num_1q_gates
        # log["prop"]["gate_2q"] = num_2q_gates
        # log["prop"]["transfer"] = num_transfer
        # log["prop"]["depth"] = depth
        # log["prop"]["compilation_time"] = time() - start
        # log["prop"]['max_ancilla'] = 0
        # log["code"] = code


def grid_distance(i, j, n_column):
    i_row = i // n_column
    i_column = i % n_column
    j_row = j // n_column
    j_column = j % n_column

    return np.sqrt((i_row - j_row) ** 2 + (i_column - j_column) ** 2)


class SimpleHeuristicCompiler(object):
    def __init__(self, configs) -> None:
        self.configs = configs

    def run(self, benchmark_sets, hyperparam_sets):
        res_list = []
        for benchmark in benchmark_sets.all_benchmarks:
            for hyperparams in hyperparam_sets.all_sets:
                log = self.compile(benchmark.circ, hyperparams)
                if self.configs.compiler.print_log:
                    print(log)
                analyzer = Analyzer(log, hyperparams, benchmark)
                report = analyzer.analyze()
                report["hyperparams"] = hyperparams.__dict__.copy()
                report["path"] = benchmark.path
                res_list.append(report)

        yaml.dump(res_list, open(f"{hyperparam_sets.configs.result_path}/res.yml", "w"))

        return res_list

    def compile(self, circ, hyperparams):
        start = time()
        # assume the simple mapping from [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] to [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # the mapping is not specified here, so the there will be no layout
        circ = transpile(
            circ,
            basis_gates=["cz", "id", "u1", "u2", "u3"],
            optimization_level=3,
            layout_method="sabre",
            routing_method="sabre",
        )

        logger = HeuristicCompilerLogger(
            circ,
            hyperparams.n_rows,
            hyperparams.n_cols,
            hyperparams.n_aods,
            hyperparams,
        )

        log = logger.get_log()
        log["compilation_time"] = time() - start

        print(circ.count_ops())

        return log

    # while True:
    #     add_layer_2 = False
    #     add_layer_1 = False
    #     front_layer = dag.front_layer()
    #     for node in front_layer:
    #         if node.op.num_qubits == 1:
    #             dag.remove_op_node(node)
    #             num_1q_gates += 1
    #             add_layer_1 = True
    #     if dag.depth() == 0:
    #         break
    #     for node in front_layer:
    #         if node.op.num_qubits == 2:
    #             num_2q_gates += 1
    #             dag.remove_op_node(node)
    #             distance += grid_distance(node.qargs[0].index, node.qargs[1].index, n_column=N_COLUMN)

    #     if add_layer_1:
    #         num_layers_1 += 1
    #     if dag.depth() == 0:
    #         break
