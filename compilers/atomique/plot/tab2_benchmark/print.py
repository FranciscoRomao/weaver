import yaml

file_path = "results/tab2_benchmark/fpqac/res.yml"
with open(file_path, "r") as file:
    res_list = yaml.load(file, Loader=yaml.FullLoader)
for res in res_list:
    name = res["benchmark"]
    n_qubits = res["others"]["n_qubits"]
    n_2q_gates = res["others"]["n_2q_gates_before_transpilation"]
    n_1q_gates = res["others"]["n_1q_gates_before_transpilation"]
    degree = res["others"]["degree"]
    n_2q_gate_per_q = 2 * n_2q_gates / n_qubits
    print(
        f"name : {name}, n_qubits : {n_qubits}, n_2q_gates : {n_2q_gates}, n_1q_gates : {n_1q_gates},  n_2q_gate_per_q : {n_2q_gate_per_q},degree : {degree}\n"
    )
