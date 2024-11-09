import os

import matplotlib.pyplot as plt
import numpy as np

from plot.plot_utils import plot_bars, tight_figure

if __name__ == "__main__":
    # two rows, 1 column
    fig, ax = plt.subplots(3, 1, figsize=(7.5, 6))
    plt.subplots_adjust(hspace=0.3)
    plt.rcParams["hatch.linewidth"] = 2
    # plt.rcParams['font.family'] = 'DejaVu Sans'

    from matplotlib import rc

    # rc('font',**{'family':'Liberation Sans'})

    paths = ["14_solver_comp/arb", "14_solver_comp/qsim", "14_solver_comp/qaoa"]
    compilers = ["solver", "simple_heuristic", "fpqac"]
    compiler_names = ["Tan-Solver", "Tan-Heuristic", "FPQA-C"]
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
        y_second_level_name="total_fidelity",
        y_label="Fidelity",
        plot_legend=True,
        geo_mean=True,
        y_lim=[0.25, 1.0],
        keep_digits=2,
        plot_xticks=False,
        rotation=90,
    )

    plot_bars(
        ax[1],
        paths=paths,
        compilers=compilers,
        compiler_names=compiler_names,
        benchs=benchs,
        y_first_level_name="circ_stats",
        y_second_level_name="n_2q_gate",
        y_label="Number of 2Q Gates",
        # y_lim=[0, 2000],
        geo_mean=False,
        keep_digits=0,
        plot_xticks=False,
        rotation=90,
    )

    plot_bars(
        ax[2],
        paths=paths,
        compilers=compilers,
        compiler_names=compiler_names,
        benchs=benchs,
        y_first_level_name="circ_stats",
        y_second_level_name="compilation_time",
        y_label="Compilation Time",
        # y_lim=[0, 2000],
        is_y_log=True,
        geo_mean=False,
        keep_digits=2,
        plot_xticks=True,
        rotation=90,
    )

    script_dir = os.path.dirname(__file__)

    save_path = os.path.join(script_dir, "solver_comp_bar.pdf")

    fig.savefig(save_path, bbox_inches="tight")
