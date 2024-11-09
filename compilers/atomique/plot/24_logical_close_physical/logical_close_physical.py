import os

import matplotlib.pyplot as plt
import numpy as np
import yaml

from plot.plot_utils import patterns, plot_improvements

if __name__ == "__main__":
    plt, ax = plt.subplots(5, figsize=(5, 4.5))
    plt.subplots_adjust(wspace=0.3, hspace=0.4)

    compiler_names = [
        "AOD Size $6\\times 6$",
        "AOD Size $8\\times 8$",
        "AOD Size $10\\times 10$",
    ]

    benchs = ["QAOA-rand-100", "QSIM-rand-100", "Phase-Code-100"]
    benchmarks = {}

    for k, benchmark in enumerate(benchs):
        benchmarks[str(k)] = ("", benchmark)

    baselines = {}
    for k, compiler in enumerate(compiler_names):
        baselines[str(k)] = ("", compiler_names[k])

    data_overlap = []
    data_distance = []
    data_2q = []
    data_depth = []
    data_time = []

    with open("results/24_logical_close_physical/default/res.yml", "r") as file:
        res_list = yaml.load(file, Loader=yaml.FullLoader)
        for info in res_list:
            data_distance.append(info["circ_stats"]["avg_move_distance"])
            data_2q.append(info["circ_stats"]["n_2q_gate"])
            data_depth.append(info["circ_stats"]["n_2q_layer"])
            data_time.append(info["time"]["total_time"])
            data_overlap.append(info["others"]["total_overlap"])

    data_distance = np.array(data_distance).reshape((len(benchs), -1)).T
    data_2q = np.array(data_2q).reshape((len(benchs), -1)).T
    data_depth = np.array(data_depth).reshape((len(benchs), -1)).T
    data_time = np.array(data_time).reshape((len(benchs), -1)).T
    data_overlap = np.array(data_overlap).reshape((len(benchs), -1)).T
    plot_improvements(
        ax[0],
        benchmarks=benchmarks,
        baselines=baselines,
        hardwares={"0": ("0", "0")},
        improvements=data_distance,
        ylabel="Move Dist.",
        colors=["#F8B62D", "#00AEBB", "#0081CC", "#A31F34", "#8A8B8C", "#70ae47"],
        patterns=patterns,
        ylog=False,
        plot_legend=True,
        geo_mean=True,
        keep_digits=4,
        plot_xticks=False,
        ncol=2,
    )
    plot_improvements(
        ax[1],
        benchmarks=benchmarks,
        baselines=baselines,
        hardwares={"0": ("0", "0")},
        improvements=data_2q,
        ylabel="2Q Gate",
        colors=["#F8B62D", "#00AEBB", "#0081CC", "#A31F34", "#8A8B8C", "#70ae47"],
        patterns=patterns,
        ylog=False,
        plot_legend=False,
        geo_mean=True,
        keep_digits=4,
        plot_xticks=False,
        ncol=2,
    )
    plot_improvements(
        ax[2],
        benchmarks=benchmarks,
        baselines=baselines,
        hardwares={"0": ("0", "0")},
        improvements=data_depth,
        ylabel="Depth",
        colors=["#F8B62D", "#00AEBB", "#0081CC", "#A31F34", "#8A8B8C", "#70ae47"],
        patterns=patterns,
        ylog=False,
        plot_legend=False,
        geo_mean=True,
        keep_digits=4,
        plot_xticks=False,
        ncol=2,
    )
    plot_improvements(
        ax[3],
        benchmarks=benchmarks,
        baselines=baselines,
        hardwares={"0": ("0", "0")},
        improvements=data_time,
        ylabel="Time",
        colors=["#F8B62D", "#00AEBB", "#0081CC", "#A31F34", "#8A8B8C", "#70ae47"],
        patterns=patterns,
        ylog=False,
        plot_legend=False,
        geo_mean=True,
        keep_digits=4,
        plot_xticks=False,
        ncol=2,
    )
    plot_improvements(
        ax[4],
        benchmarks=benchmarks,
        baselines=baselines,
        hardwares={"0": ("0", "0")},
        improvements=data_overlap,
        ylabel="Overlap",
        colors=["#F8B62D", "#00AEBB", "#0081CC", "#A31F34", "#8A8B8C", "#70ae47"],
        patterns=patterns,
        ylog=False,
        plot_legend=False,
        geo_mean=True,
        keep_digits=4,
        plot_xticks=True,
        ncol=2,
    )

    script_dir = os.path.dirname(__file__)

    save_path = os.path.join(script_dir, "ablation_logical_close_physical.pdf")

    plt.savefig(save_path, bbox_inches="tight")
