import os

import matplotlib.pyplot as plt

from plot.plot_utils import plot_2d_breakdown_fill, plot_2d_curve

if __name__ == "__main__":
    # import pdb
    # pdb.set_trace()

    first_level_names = [
        "hyperparams",
        "circ_stats",
        "hyperparams",
        "hyperparams",
        "hyperparams",
        "hyperparams",
    ]
    variables = [
        "T_per_move",
        "avg_move_speed",
        "atom_distance",
        "cooling_deltaN_thres",
        "na_T1",
        "na_2Q_fidelity",
    ]
    x_labels = [
        "Time per Move (us)",
        "Average Move Speed (m/s)",
        "Atom Distance (um)",
        "N_vibration Threshold for Cooling",
        "Coherence Time (s)",
        "2Q Gate Fidelity",
    ]
    alphas = ["a", "b", "c", "d", "e", "f"]
    x_scales = [1e-6, 1, 1e-6, 1, 1, 1]
    inset_sizes = [
        ["70%", "70%"],
        ["50%", "50%"],
        ["50%", "50%"],
        ["50%", "50%"],
        ["50%", "50%"],
        ["50%", "50%"],
    ]
    inset_locs = [1, 2, 1, 1, 1, 1]
    ylims = [None, [0, 6], [0, 2], [0, 6], [0, 6], [0, 6]]
    is_y_logs = [False, False, False, False, False, False]
    is_x_logs = [False, False, False, False, True, False]
    special_x_logs = [False, False, False, False, False, True]

    # first_level_names = ['circ_stats']
    # variables = ['avg_move_speed']
    # x_labels = ['Average move speed (um/s)']
    # x_scales = [1]
    # inset_sizes = [["50%", "50%"]]
    # inset_locs = [2]
    # import pdb
    # pdb.set_trace()
    plt.rcParams["font.size"] = 16
    fig, ax = plt.subplots(2, 6, figsize=(22, 7.5))
    plt.subplots_adjust(wspace=0.23, hspace=0.43)

    for i in range(len(variables)):
        variable = variables[i]
        # plt.clf()

        plot_2d_curve(
            ax[0][i],
            n_series=3,
            compilers=["faa", "geyser", "fpqac"],
            paths=[
                f"results/19_sensitivity/{variable}/arb",
                f"results/19_sensitivity/{variable}/qsim",
                f"results/19_sensitivity/{variable}/qaoa",
            ],
            x_first_level_name=first_level_names[i],
            x_second_level_name=variable,
            y_first_level_name="fidelity",
            y_second_level_name="total_fidelity",
            is_x_log=is_x_logs[i],
            is_y_log=is_y_logs[i],
            benchs=["BV70", "QSim-rand-20", "QAOA-regu5-40"],
            compiler_names=["FAA-Rectangular", "FAA-Triangular", "FPQA-C"],
            xlabel=x_labels[i],
            ylabel="Fidelity" if i == 0 else None,
            xlim=None,
            ylim=None,
            plot_legend=i == 0,
            x_scale=x_scales[i],
            special_x_log=special_x_logs[i],
        )

        plot_2d_breakdown_fill(
            ax[1][i],
            compiler="fpqac",
            path=f"results/19_sensitivity/{variable}/arb",
            x_first_level_name=first_level_names[i],
            x_second_level_name=variable,
            breakdown_parts_first_level_name="fidelity",
            breakdown_parts_second_level_name=[
                "1q_total",
                "2q_total",
                "additional_2Q_error_by_heating",
                "additional_2Q_by_cooling",
                "movement_atomloss",
                "movement_decoherence",
            ],
            breakdown_name=[
                "1Q Gate",
                "2Q Gate",
                "Move Heating",
                "Move Cooling",
                "Move Atom Loss",
                "Move Decoherence",
            ],
            is_x_log=is_x_logs[i],
            is_y_log=False,
            bench="BV70",
            compiler_name="FPQA-C",
            xlabel=f"{x_labels[i]}\n({alphas[i]})",
            ylabel="-Log(Fidelity)" if i == 0 else None,
            xlim=None,
            ylim=ylims[i],
            ylim_inset=[0, 0.3],
            inset_loc=inset_locs[i],
            inset_size=inset_sizes[i],
            plot_legend=i == 0,
            x_scale=x_scales[i],
            special_x_log=special_x_logs[i],
        )

        # plt.tight_layout()
        # plt.xscale('log')
        script_dir = os.path.dirname(__file__)

        save_path = os.path.join(script_dir, "ablation_2d_all.pdf")

        fig.savefig(save_path, bbox_inches="tight")
