import os

import matplotlib.pyplot as plt

from plot.plot_utils import plot_2d_breakdown_fill, plot_2d_curve


def get_n_row_col(n_qubits):
    n_rows = []
    n_cols = []
    for i in range(n_qubits, 0, -1):
        n_col = int(n_qubits // i)
        if len(n_cols) == 0 or n_col != n_cols[-1]:
            n_rows.append(i)
            n_cols.append(n_col)
    return n_rows, n_cols


def get_n_row_col_2(n_start, n_end):
    return list(range(n_start, n_end)), list(range(n_start, n_end))


def process_n_row_col(n_rows, n_cols):
    strings = []
    for nr, nc in zip(n_rows, n_cols):
        strings.append(f"{nr} X {nc}")
    return strings


def plot1(size_setting):
    # import pdb
    # pdb.set_trace()
    n_atoms_per_array = 49
    first_level_names = ["hyperparams"] * 4
    variables = ["n_rows"] * 4
    x_labels = ["Atom Array Topology"] * 4
    # x_scales = [1e-6, 1, 1e-6, 1, 1]
    # ylims = [None, [0, 6], [0, 2], [0, 6], [0, 6]]
    is_y_logs = [False, False, False, False, False]
    is_x_logs = [False, False, False, False, False]
    y_labels = [
        "Execution Time",
        "Fidelity",
        "Avg. Moving Distance",
        "Number of 2Q Gates",
    ]
    # y_first_level_names = ['circ_stats', 'circ_stats', 'circ_stats']
    # y_second_level_names = ['each_move_distance_std', 'n_move', 'each_move_distance_mean']
    y_first_level_names = ["time", "fidelity", "circ_stats", "circ_stats"]
    y_second_level_names = [
        "total_time",
        "total_fidelity",
        "avg_move_distance",
        "n_2q_gate",
    ]
    special_x_logs = [False, False, False, False, True]
    ylims = [None, None, None, None]

    fig, ax = plt.subplots(1, 4, figsize=(9.9, 2.2))
    fig.subplots_adjust(wspace=0.5)

    for i in range(0, 4):
        variable = variables[i]
        # plt.clf()
        plt.rcParams["font.size"] = 12
        if size_setting == "diff":
            x_ticks = process_n_row_col(*get_n_row_col_2(7, 21))
        else:
            x_ticks = process_n_row_col(*get_n_row_col(n_atoms_per_array))

        plot_2d_curve(
            ax[i],
            n_series=3,
            compilers=["fpqac"],
            paths=[
                f"results/20_sensitivity/{variable}_{size_setting}_size/arb",
                f"results/20_sensitivity/{variable}_{size_setting}_size/qsim",
                f"results/20_sensitivity/{variable}_{size_setting}_size/qaoa",
            ],
            x_first_level_name=first_level_names[i],
            x_second_level_name=variable,
            y_first_level_name=y_first_level_names[i],
            y_second_level_name=y_second_level_names[i],
            is_x_log=is_x_logs[i],
            is_y_log=is_y_logs[i],
            benchs=[
                "Arb-100Q",
                "QSim-40Q",
                "QAOA-40Q",
            ],
            compiler_names=["FPQA-C"] * 3,
            xlabel=x_labels[i],
            ylabel=y_labels[i],
            xlim=None,
            ylim=ylims[i],
            plot_legend=i == 0,
            x_scale=1,
            special_x_log=special_x_logs[i],
            is_catogorical=True,
            # xticks=process_n_row_col(*get_n_row_col(n_atoms_per_array)),
            xticks=x_ticks,
        )

        # plt.tight_layout()
        # plt.xscale('log')
    script_dir = os.path.dirname(__file__)

    save_path = os.path.join(
        script_dir, f"dev_ablation_2d_{variable}_{size_setting}_size.pdf"
    )

    fig.savefig(save_path, bbox_inches="tight")


def plot2():
    # import pdb
    # pdb.set_trace()
    n_atoms_per_array = 49
    first_level_names = ["hyperparams"] * 4
    variables = ["n_rows"] * 4
    x_labels = ["Number of AOD Arrays"] * 4
    # x_scales = [1e-6, 1, 1e-6, 1, 1]
    # ylims = [None, [0, 6], [0, 2], [0, 6], [0, 6]]
    is_y_logs = [False, False, False, False, False]
    is_x_logs = [False, False, False, False, False]
    y_labels = [
        "Execution Time",
        "Fidelity",
        "Avg. Moving Distance",
        "Number of 2Q Gates",
    ]
    # y_first_level_names = ['circ_stats', 'circ_stats', 'circ_stats']
    # y_second_level_names = ['each_move_distance_std', 'n_move', 'each_move_distance_mean']
    y_first_level_names = ["time", "fidelity", "circ_stats", "circ_stats"]
    y_second_level_names = [
        "total_time",
        "total_fidelity",
        "avg_move_distance",
        "n_2q_gate",
    ]
    special_x_logs = [False, False, False, False, True]
    ylims = [None, None, None, None]
    size_setting = "diff"

    fig, ax = plt.subplots(1, 4, figsize=(9.9, 2.2))
    fig.subplots_adjust(wspace=0.5)

    for i in range(0, 4):
        variable = variables[i]
        # plt.clf()
        plt.rcParams["font.size"] = 12
        plot_2d_curve(
            ax[i],
            n_series=3,
            compilers=["fpqac"],
            paths=[
                f"results/20_sensitivity/n_aods/arb",
                f"results/20_sensitivity/n_aods/qsim",
                f"results/20_sensitivity/n_aods/qaoa",
            ],
            x_first_level_name=first_level_names[i],
            x_second_level_name=variable,
            y_first_level_name=y_first_level_names[i],
            y_second_level_name=y_second_level_names[i],
            is_x_log=is_x_logs[i],
            is_y_log=is_y_logs[i],
            benchs=[
                "Arb-100Q",
                "QSim-40Q",
                "QAOA-40Q",
            ],
            compiler_names=["FPQA-C"] * 3,
            xlabel=x_labels[i],
            ylabel=y_labels[i],
            xlim=None,
            ylim=ylims[i],
            plot_legend=i == 0,
            x_scale=1,
            special_x_log=special_x_logs[i],
            is_catogorical=True,
            # xticks=process_n_row_col(*get_n_row_col(n_atoms_per_array)),
            xticks=[1, 2, 3, 4, 5, 6, 7],
        )

        # plt.tight_layout()
        # plt.xscale('log')
    script_dir = os.path.dirname(__file__)

    save_path = os.path.join(script_dir, "dev_ablation_2d_n_aods.pdf")

    fig.savefig(save_path, bbox_inches="tight")


if __name__ == "__main__":
    plot1("diff")
    plot1("same")
    plot2()
