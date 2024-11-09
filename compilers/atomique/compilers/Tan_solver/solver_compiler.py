import json
from functools import partial
from multiprocessing import Pool
from pathlib import Path

from qiskit import transpile

from compilers.analyzer import Analyzer
from compilers.Tan_solver.solve import DPQA
from utils import Position

solved_benchmarks = [
    "benchmarks_qsim_molecule_H2",
    "benchmarks_supermarq_supermarq_bit_code_n20",
    "benchmarks_supermarq_supermarq_mermin_bell_n5",
    "benchmarks_supermarq_supermarq_vqe_proxy_n5",
    "benchmarks_supermarq_supermarq_vqe_proxy_n10",
    "benchmarks_qaoa_regular_q10_regular3_i0",
    "benchmarks_qaoa_regular_q10_regular3_i1",
    "benchmarks_qaoa_regular_q10_regular3_i2",
    "benchmarks_qaoa_regular_q10_regular3_i3",
    "benchmarks_qaoa_regular_q10_regular3_i4",
    "benchmarks_qaoa_regular_q10_regular3_i5",
    "benchmarks_qaoa_regular_q10_regular3_i6",
    "benchmarks_qaoa_regular_q10_regular3_i7",
    "benchmarks_qaoa_regular_q10_regular3_i8",
    "benchmarks_qaoa_regular_q10_regular3_i9",
    "benchmarks_qaoa_rand_q5_p0.5_i0",
    "benchmarks_qaoa_rand_q5_p0.5_i1",
    "benchmarks_qaoa_regular_q6_regular4_i0",
    "benchmarks_qaoa_regular_q6_regular4_i1",
    "benchmarks_qaoa_regular_q6_regular4_i2",
    "benchmarks_qaoa_regular_q6_regular4_i3",
    "benchmarks_qaoa_regular_q6_regular4_i4",
    "benchmarks_qaoa_regular_q6_regular4_i5",
    "benchmarks_qaoa_regular_q6_regular4_i6",
    "benchmarks_qaoa_regular_q6_regular4_i7",
    "benchmarks_qaoa_regular_q6_regular4_i8",
    "benchmarks_qaoa_regular_q6_regular4_i9",
    "benchmarks_qaoa_regular_q10_regular4_i0",
    "benchmarks_qaoa_regular_q10_regular4_i1",
    "benchmarks_qaoa_regular_q10_regular4_i2",
    "benchmarks_qaoa_regular_q10_regular4_i3",
    "benchmarks_qaoa_regular_q10_regular4_i4",
    "benchmarks_qaoa_regular_q10_regular4_i5",
    "benchmarks_qaoa_regular_q10_regular4_i6",
    "benchmarks_qaoa_regular_q10_regular4_i7",
    "benchmarks_qaoa_regular_q10_regular4_i8",
    "benchmarks_qaoa_regular_q10_regular4_i9",
    "benchmarks_arbitrary_rand_q5_g10_i4",
    "benchmarks_arbitrary_rand_q5_g10_i5",
    "benchmarks_arbitrary_rand_q5_g10_i6",
    "benchmarks_arbitrary_rand_q5_g10_i7",
    "benchmarks_arbitrary_rand_q5_g10_i8",
    "benchmarks_arbitrary_rand_q5_g10_i9",
    "benchmarks_qsim_rand_q5_10_p0.3_i0",
    "benchmarks_qsim_rand_q5_10_p0.3_i1",
    "benchmarks_qsim_rand_q5_10_p0.3_i2",
    "benchmarks_qsim_rand_q5_10_p0.3_i3",
    "benchmarks_qsim_rand_q5_10_p0.3_i4",
    "benchmarks_qsim_rand_q5_10_p0.3_i5",
    "benchmarks_qsim_rand_q5_10_p0.3_i6",
    "benchmarks_qsim_rand_q5_10_p0.3_i7",
    "benchmarks_qsim_rand_q5_10_p0.3_i8",
    "benchmarks_qsim_rand_q5_10_p0.3_i9",
    "benchmarks_qsim_rand_q5_10_p0.5_i0",
    "benchmarks_qsim_rand_q5_10_p0.5_i1",
    "benchmarks_qsim_rand_q5_10_p0.5_i2",
    "benchmarks_qsim_rand_q5_10_p0.5_i3",
    "benchmarks_qsim_rand_q5_10_p0.5_i8",
    "benchmarks_qsim_rand_q5_10_p0.5_i9",
    "benchmarks_qaoa_regular_q20_regular3_i0",
    "benchmarks_qaoa_regular_q20_regular3_i1",
    "benchmarks_qaoa_regular_q20_regular3_i2",
    "benchmarks_qaoa_regular_q20_regular3_i3",
    "benchmarks_qaoa_regular_q20_regular3_i4",
    "benchmarks_qaoa_regular_q20_regular3_i5",
    "benchmarks_qaoa_regular_q20_regular3_i6",
    "benchmarks_qaoa_regular_q20_regular3_i7",
    "benchmarks_qaoa_regular_q20_regular3_i8",
    "benchmarks_qaoa_regular_q20_regular3_i9",
    "benchmarks_qaoa_rand_q10_p0.5_i1",
    "benchmarks_qaoa_rand_q10_p0.5_i2",
    "benchmarks_qaoa_rand_q10_p0.5_i4",
    "benchmarks_qaoa_rand_q10_p0.5_i5",
    "benchmarks_qaoa_rand_q10_p0.5_i6",
    "benchmarks_qaoa_rand_q10_p0.5_i9",
    "benchmarks_qsim_rand_q10_10_p0.3_i0",
    "benchmarks_qsim_rand_q10_10_p0.3_i1",
    "benchmarks_qsim_rand_q10_10_p0.3_i2",
    "benchmarks_qsim_rand_q10_10_p0.3_i3",
    "benchmarks_qsim_rand_q10_10_p0.3_i4",
    "benchmarks_qsim_rand_q10_10_p0.3_i5",
    "benchmarks_qsim_rand_q10_10_p0.3_i6",
    "benchmarks_qsim_rand_q10_10_p0.3_i7",
    "benchmarks_qsim_rand_q10_10_p0.3_i8",
    "benchmarks_qsim_rand_q10_10_p0.3_i9",
    "benchmarks_supermarq_supermarq_vqe_proxy_n20",
    "benchmarks_supermarq_supermarq_vqe_proxy_n30",
    "benchmarks_supermarq_supermarq_qaoa_vanilla_proxy_n5",
    "benchmarks_qaoa_regular_q6_regular3_i0",
    "benchmarks_qaoa_regular_q6_regular3_i1",
    "benchmarks_qsim_rand_q10_10_p0.5_i1",
    "benchmarks_qsim_rand_q10_10_p0.5_i2",
    "benchmarks_qsim_rand_q10_10_p0.5_i3",
    "benchmarks_qsim_rand_q10_10_p0.5_i8",
    "benchmarks_qsim_rand_q10_10_p0.5_i9",
    "benchmarks_qsim_rand_q10_10_p0.5_i4",
    "benchmarks_qsim_rand_q10_10_p0.5_i5",
    "benchmarks_qsim_rand_q10_10_p0.5_i6",
    "benchmarks_qsim_rand_q10_10_p0.5_i7",
    "benchmarks_qaoa_regular_q6_regular3_i6",
    "benchmarks_qaoa_regular_q6_regular3_i7",
    "benchmarks_qaoa_regular_q6_regular3_i8",
    "benchmarks_qaoa_regular_q6_regular3_i9",
    "benchmarks_qaoa_regular_q6_regular3_i2",
    "benchmarks_qaoa_regular_q6_regular3_i3",
    "benchmarks_qaoa_regular_q6_regular3_i4",
    "benchmarks_qaoa_regular_q6_regular3_i5",
    "benchmarks_qaoa_rand_q5_p0.5_i6",
    "benchmarks_qaoa_rand_q5_p0.5_i7",
    "benchmarks_qaoa_rand_q5_p0.5_i8",
    "benchmarks_qaoa_rand_q5_p0.5_i9",
    "benchmarks_qaoa_rand_q5_p0.5_i2",
    "benchmarks_qaoa_rand_q5_p0.5_i3",
    "benchmarks_qaoa_rand_q5_p0.5_i4",
    "benchmarks_qaoa_rand_q5_p0.5_i5",
    "benchmarks_arbitrary_rand_q5_g10_i0",
    "benchmarks_arbitrary_rand_q5_g10_i1",
    "benchmarks_arbitrary_rand_q5_g10_i2",
    "benchmarks_arbitrary_rand_q5_g10_i3",
    "benchmarks_qsim_rand_q5_10_p0.5_i4",
    "benchmarks_qsim_rand_q5_10_p0.5_i5",
    "benchmarks_qsim_rand_q5_10_p0.5_i6",
    "benchmarks_qsim_rand_q5_10_p0.5_i7",
    "benchmarks_qsim_rand_q20_10_p0.3_i0",
    "benchmarks_qsim_rand_q20_10_p0.3_i1",
    "benchmarks_qsim_rand_q20_10_p0.3_i2",
    "benchmarks_qsim_rand_q20_10_p0.3_i3",
    "benchmarks_qsim_rand_q20_10_p0.3_i4",
    "benchmarks_qsim_rand_q20_10_p0.3_i5",
    "benchmarks_qsim_rand_q20_10_p0.3_i6",
    "benchmarks_qsim_rand_q20_10_p0.3_i7",
    "benchmarks_qsim_rand_q20_10_p0.3_i8",
    "benchmarks_qsim_rand_q20_10_p0.3_i9",
    "benchmarks_algorithm_adder_n4",
    "benchmarks_algorithm_adder_n10",
    "benchmarks_algorithm_bv_n14",
    "benchmarks_algorithm_dnn_n8",
    "benchmarks_algorithm_ising_n10",
    "benchmarks_algorithm_ising_n34",
    "benchmarks_algorithm_shor_n5",
    "benchmarks_qsim_rand_q10_10_p0.5_i0",
]

timeout_benchmarks = [
    "benchmarks_qaoa_rand_q10_p0.5_i0",
    "benchmarks_qaoa_rand_q10_p0.5_i3",
    "benchmarks_qaoa_rand_q10_p0.5_i8",
    "benchmarks_qaoa_rand_q10_p0.5_i7",
]


def get_rel_pos(q):
    if q["a"] == 0:
        return Position(x=q["x"], y=q["y"], z=-1)
    else:
        return Position(x=q["c"], y=q["r"], z=0)


def deduce_aod_pos_code(n_c, n_r, layer):
    aod_col_pos = [-1 for _ in range(n_c)]
    aod_row_pos = [-1 for _ in range(n_r)]
    for q in layer["qubits"]:
        if q["a"] == 1:
            aod_col_pos[q["c"]] = q["x"]
            aod_row_pos[q["r"]] = q["y"]
    for col in range(n_c):
        if aod_col_pos[col] == -1:
            if col == 0:
                aod_col_pos[col] = 0
            else:
                aod_col_pos[col] = aod_col_pos[col - 1]
    for row in range(n_r):
        if aod_row_pos[row] == -1:
            if row == 0:
                aod_row_pos[row] = 0
            else:
                aod_row_pos[row] = aod_row_pos[row - 1]
    return {
        "type": "move",
        "data": {
            "ancilla_abs_pos_x": [
                aod_col_pos,
            ],
            "ancilla_abs_pos_y": [
                aod_row_pos,
            ],
        },
    }


def deduce_2Q_gate_qubits(layer):
    involved_qubits = []
    for g in layer["gates"]:
        involved_qubits.append(g["q0"])
        involved_qubits.append(g["q1"])
    qubit_rel_pos = [get_rel_pos(layer["qubits"][q]) for q in involved_qubits]

    return (
        involved_qubits,
        qubit_rel_pos,
        {
            "type": "gate_2Q",
            "additional_stage": 0,
            "data": [
                {"source": qubit_rel_pos[r], "ancilla": qubit_rel_pos[r + 1]}
                for r in range(0, len(qubit_rel_pos), 2)
            ],
        },
    )


def get_g_q(circ):
    circ = transpile(circ, basis_gates=["cz", "id", "u2", "u1", "u3"])
    g_q = []
    for inst in circ._data:
        op = inst.operation
        if op.name == "u3" or op.name == "u2":
            g_q.append((inst[1][0].index,))
        if op.name == "cz":
            g_q.append(
                [
                    min(inst[1][0].index, inst[1][1].index),
                    max(inst[1][0].index, inst[1][1].index),
                ]
            )
    return g_q


class SolverCompiler:
    def __init__(self, configs, result_dir: str = None, solve=False) -> None:
        self.configs = configs
        self.solve = solve
        self.result_dir = result_dir
        # self.parallelism = 1

    def run(self, benchmark_sets, hyperparam_sets):
        res_list = []
        compilation_times = []
        for hyperparams in hyperparam_sets.all_sets:
            # pool = Pool(self.parallelism)

            logs = [self.compile(b, hyperparams) for b in benchmark_sets.all_benchmarks]

            for bench, log in enumerate(logs):
                if self.configs.compiler.print_log:
                    print(log)
                analyzer = Analyzer(
                    log, hyperparams, benchmark_sets.all_benchmarks[bench]
                )
                report = analyzer.analyze()
                res_list.append(report)
                # print(report)
                compilation_times.append(log["compilation_time"])
        print(compilation_times)
        return res_list

    def run_solver(self, name, benchmark):
        solver = DPQA(name, print_detail=False, dir="compilers/Tan_solver/try/")
        solver.setOptimalRatio(self.configs.compiler.optimal_ratio)
        solver.setNoTransfer()
        solver.setArchitecture([self.n_c, self.n_r, self.n_c, self.n_r])

        if "H2" in benchmark.__repr__():
            n_qubits = 4
        elif "LiH" in benchmark.__repr__():
            n_qubits = 8
        elif "supermarq_bit_code_n20" in benchmark.__repr__():
            n_qubits = 39
        else:
            n_qubits = benchmark.n_qubits

        if "qaoa" in benchmark.__repr__():
            if "vanilla_proxy_n5" in benchmark.__repr__():
                edges = [
                    (0, 1),
                    (0, 2),
                    (0, 3),
                    (0, 4),
                    (1, 2),
                    (1, 3),
                    (1, 4),
                    (2, 3),
                    (2, 4),
                    (3, 4),
                ]
            else:
                edges = benchmark.edges
            g_q = [[min(edge[0], edge[1]), max(edge[0], edge[1])] for edge in edges]
            solver.setProgram(g_q, nqubit=n_qubits)
            solver.setCommutation()
        else:
            g_q = get_g_q(benchmark.circ)
            solver.setProgram([g for g in g_q if len(g) == 2], nqubit=n_qubits)

        return solver.solve(save_file=True)

    def generate_log(self, result, benchmark, hyperparams):
        if not result:
            return None
        if "H2" in benchmark.__repr__():
            n_qubits = 4
        elif "LiH_UCCSD" in benchmark.__repr__():
            n_qubits = 8
        else:
            n_qubits = benchmark.n_qubits
        layers = result["layers"]
        log = {
            "compilation_time": result["duration"],
            "prop": {
                "n_qubits": n_qubits,
                "max_ancilla": 0,
                "slm_rel_pos": [
                    get_rel_pos(q) for q in layers[0]["qubits"] if q["a"] == 0
                ],
            },
            "code": [
                {
                    "type": "prepare",
                    "data": [
                        {
                            "slm_rel_pos": Position(x=0, y=0, z=-1),
                            "ancilla_rel_pos": get_rel_pos(q),
                        }
                        for q in layers[0]["qubits"]
                        if q["a"] == 1
                    ],
                },
            ],
        }

        if "qaoa" in benchmark.__repr__():
            # initial all H
            log["code"].append(
                {
                    "type": "gate_1Q",
                    "data": [{"source": get_rel_pos(q)} for q in layers[0]["qubits"]],
                }
            )

            for l in range(len(layers)):

                log["code"].append(deduce_aod_pos_code(self.n_c, self.n_r, layers[l]))

                involved_qubits, qubit_loc, code_2q = deduce_2Q_gate_qubits(layers[l])
                # ZZ(\theta) = [ Rz(\theta) \otimes Rz(\theta) ] x CRz(-\theta)
                # 1Q gates (the two Rz)
                log["code"].append(
                    {
                        "type": "gate_1Q",
                        "data": [{"source": rel_pos} for rel_pos in qubit_loc],
                    }
                )
                # 2Q gates (CRz)
                log["code"].append(code_2q)

        else:
            num_2q = sum([len(layer["gates"]) for layer in layers])
            g_q = get_g_q(benchmark.circ)
            now_num_2q = 0
            for g in g_q:
                if len(g) == 2:
                    now_num_2q += 1
            if now_num_2q != num_2q:
                raise ValueError(
                    f"number of 2Q gates in the solved result {num_2q} and now"
                    f" (after transpiling again) {now_num_2q} are different!"
                )
            for l in range(len(layers)):
                # which gates are executed
                executed = [0 for _ in range(len(g_q))]
                codes_1q = [
                    [0 for _ in range(n_qubits)],
                ]
                involved_qubits, qubit_loc, code_2q = deduce_2Q_gate_qubits(layers[l])

                upper_bound = [-1 for _ in range(n_qubits)]
                # which 2Q gates are being executed
                for g in range(0, len(involved_qubits), 2):
                    for gg in range(len(g_q)):
                        if (
                            len(g_q[gg]) == 2
                            and involved_qubits[g] == g_q[gg][0]
                            and involved_qubits[g + 1] == g_q[gg][1]
                        ):
                            executed[gg] = 1
                            upper_bound[g_q[gg][0]] = gg
                            upper_bound[g_q[gg][1]] = gg
                            break

                # which 1Q gates must be before these 2Q gates
                for gg in range(len(g_q)):
                    if (
                        len(g_q[gg]) == 1
                        and g_q[gg][0] in involved_qubits
                        and gg < upper_bound[g_q[gg][0]]
                    ):
                        q = g_q[gg][0]
                        executed[gg] = 1
                        if codes_1q[-1][q] != 0:
                            codes_1q.append([0 for _ in range(n_qubits)])
                        for code in codes_1q:
                            if code[q] == 0:
                                code[q] = 1
                                break

                log["code"].append(deduce_aod_pos_code(self.n_c, self.n_r, layers[l]))

                for code in codes_1q:
                    if 1 in code:
                        log["code"].append(
                            {
                                "type": "gate_1Q",
                                "data": [
                                    {"source": get_rel_pos(layers[l]["qubits"][q])}
                                    for q in range(n_qubits)
                                    if code[q] == 1
                                ],
                            }
                        )
                log["code"].append(code_2q)

                new_g_q = [g_q[gg] for gg in range(len(g_q)) if executed[gg] == 0]
                g_q = new_g_q

        return log

    def compile(self, benchmark, hyperparams=None):
        # print(benchmark.circ)
        self.n_c = hyperparams.n_cols
        self.n_r = hyperparams.n_rows

        name = benchmark.__repr__().replace("/", "_")
        name = name.replace(".txt", "")
        name = name.replace(".qasm", "")

        saved_result_file = "compilers/Tan_solver/paper/" + name + ".json"

        if self.solve:
            print(f"run solver on {name}")
            if Path(saved_result_file).exists():
                print(f"{saved_result_file} already exists.")
                return None
            else:
                # self.run_solver(name, benchmark)
                # return None
                return self.generate_log(
                    self.run_solver(name, benchmark), benchmark, hyperparams
                )
        if name in solved_benchmarks:
            print(f"found solved file for {name}")
            with open(saved_result_file, "r") as f:
                smt_dict = json.load(f)
            # self.generate_log(smt_dict, benchmark, hyperparams)
            try:
                log = self.generate_log(smt_dict, benchmark, hyperparams)
                return log
            except:
                print(f"2Q gate num mismatch {benchmark.__repr__()}")
        elif name in timeout_benchmarks:
            print(f"{name} is known to timeout")
            return None
        else:
            raise ValueError(
                f"We should have decided not to include {name} in the solver results."
            )
