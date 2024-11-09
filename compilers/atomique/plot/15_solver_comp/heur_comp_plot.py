import os

import matplotlib.pyplot as plt
import numpy as np

from plot.plot_utils import plot_bars, tight_figure

if __name__ == "__main__":
    # two rows, 1 column
    fig, ax = plt.subplots(2, 1, figsize=(7.5, 3))
    plt.subplots_adjust(hspace=0.4)
    plt.rcParams["hatch.linewidth"] = 2
    # plt.rcParams['font.family'] = 'DejaVu Sans'

    from matplotlib import rc

    # rc('font',**{'family':'Liberation Sans'})

    paths = ["15_solver_comp/arb", "15_solver_comp/qsim", "15_solver_comp/qaoa"]
    compilers = ["simple_heuristic", "fpqac"]
    compiler_names = ["Tan-Heuristic", "FPQA-C"]
    benchs = [
        "Mermin-Bell-5",
        "VQE-10",
        "VQE-20",
        "Adder-10",
        "BV-14",
        "QSim-rand-5",
        "QSim-rand-10",
        "H2-4",
        "QAOA-rand-5",
        "QAOA-regu3-20",
        "QAOS-regu4-10",
    ]

    plot_bars(
        ax[0],
        paths=paths,
        compilers=compilers,
        compiler_names=compiler_names,
        benchs=benchs,
        y_first_level_name="fidelity",
        y_second_level_name="2q_total",
        y_label="2Q Gates Fid.",
        plot_legend=True,
        geo_mean=False,
        # y_lim=[0, 1.0],
        keep_digits=2,
        plot_xticks=False,
    )

    plot_bars(
        ax[1],
        paths=paths,
        compilers=compilers,
        benchs=benchs,
        compiler_names=compiler_names,
        y_first_level_name="fidelity",
        y_second_level_name="transfer_total",
        y_label="Atom Transfer Fid.",
        plot_legend=False,
        geo_mean=True,
        # y_lim=[0.8, 1.0],
        keep_digits=2,
        plot_xticks=True,
    )

    script_dir = os.path.dirname(__file__)

    save_path = os.path.join(script_dir, "heur_comp_bar.pdf")

    fig.savefig(save_path, bbox_inches="tight")
