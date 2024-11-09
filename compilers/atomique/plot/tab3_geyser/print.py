import yaml

file_path = "results/tab3_geyser/fpqac/res.yml"
with open(file_path, "r") as file:
    res_list = yaml.load(file, Loader=yaml.FullLoader)
for res in res_list:
    print(res["benchmark"], res["circ_stats"]["n_2q_gate"] * 3)
