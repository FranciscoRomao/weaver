import os

import matplotlib.pyplot as plt
import numpy as np
import yaml

from plot.plot_utils import colors, patterns, plot_improvements

if __name__ == "__main__":

    plt, ax = plt.subplots(1, figsize=(5, 2))
    plt.subplots_adjust(wspace=0.3, hspace=0.7)

    compiler_names = [
        "Baseline",
        "+Qubit Array Mapper",
        "+Qubit Array Mapper\n+ Qubit Atom Mapper",
        "+Qubit Array Mapper\n+ Qubit Atom Mapper\n+ High Parallelism Router",
    ]

    benchs = ["Arb-10", "Arb-20", "Arb-40", "Arb-100"]
    benchmarks = {}

    for k, benchmark in enumerate(benchs):
        benchmarks[str(k)] = ("", benchmark)

    baselines = {}
    for k, compiler in enumerate(compiler_names):
        baselines[str(k)] = ("", compiler_names[k])

    res_dict = {}
    # retrieve data
    data = []

    res_dict = {"arb": [], "simple_heuristic": []}

    with open("results/21_technique_breakdown/arb/fpqac/res.yml", "r") as file:
        res_list = yaml.load(file, Loader=yaml.FullLoader)
        res_dict["arb"].extend(res_list)
    for info in res_dict["arb"]:
        data.append(info["fidelity"]["total_fidelity"])
    data = np.array(data).reshape((len(benchs), -1))
    data = data.T

    print(data)

    plot_improvements(
        ax,
        benchmarks=benchmarks,
        baselines=baselines,
        hardwares={"0": ("0", "0")},
        improvements=data,
        ylabel="Fidelity",
        colors=["#F8B62D", "#00AEBB", "#0081CC", "#A31F34", "#8A8B8C", "#70ae47"],
        patterns=patterns,
        ylog=False,
        plot_legend=True,
        ylim=(0, 1.0),
        geo_mean=True,
        keep_digits=4,
        plot_xticks=True,
        ncol=2,
        rotation=90,
    )
    script_dir = os.path.dirname(__file__)

    save_path = os.path.join(script_dir, "technique_breakdown.pdf")

    plt.savefig(save_path, bbox_inches="tight")
