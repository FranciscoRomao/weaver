import os

import matplotlib.pyplot as plt

from plot.plot_utils import plot_bars, tight_figure

if __name__ == "__main__":
    fig, ax = plt.subplots(3, 1, figsize=(22, 5))
    plt.subplots_adjust(hspace=0.3)
    plt.rcParams["hatch.linewidth"] = 2

    from matplotlib import rc

    plot_bars(
        ax[0],
        y_first_level_name="circ_stats",
        y_second_level_name="n_2q_layer",
        y_label="Depth",
        # y_lim=[0, 2000],
        plot_legend=True,
        is_y_log=True,
        geo_mean=False,
        keep_digits=0,
        plot_xticks=False,
        rotation=90,
    )
    plot_bars(
        ax[1],
        y_first_level_name="circ_stats",
        y_second_level_name="n_2q_gate",
        y_label="Number of 2Q Gates",
        # y_lim=[0, 2000],
        is_y_log=True,
        geo_mean=False,
        keep_digits=0,
        plot_legend=False,
        plot_xticks=False,
        rotation=90,
    )
    plot_bars(
        ax[2],
        y_first_level_name="fidelity",
        y_second_level_name="total_fidelity",
        y_label="Fidelity",
        plot_legend=False,
        geo_mean=True,
        y_lim=[0, 1.0],
        keep_digits=3,
        plot_xticks=True,
        rotation=90,
    )

    script_dir = os.path.dirname(__file__)

    save_path = os.path.join(script_dir, "maintable_fid_n2q_depth.pdf")

    fig.savefig(save_path, bbox_inches="tight")
