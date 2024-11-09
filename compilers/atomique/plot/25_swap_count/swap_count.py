import os

import matplotlib.pyplot as plt

from plot.plot_utils import plot_bars_SWAP

if __name__ == "__main__":
    # two rows, 1 column
    fig, ax = plt.subplots(1, 1, figsize=(10, 3))
    plt.subplots_adjust(hspace=0.3)
    plt.rcParams["hatch.linewidth"] = 2
    # plt.rcParams['font.family'] = 'DejaVu Sans'

    from matplotlib import rc

    # rc('font',**{'family':'Liberation Sans'})

    plot_bars_SWAP(
        ax,
        y_first_level_name="circ_stats",
        y_second_level_name="n_2q_gate",
        y_label="Additional CNOT",
        plot_legend=True,
        is_y_log=True,
        geo_mean=False,
        keep_digits=0,
        plot_xticks=True,
    )

    # tight_figure(fig)
    script_dir = os.path.dirname(__file__)

    save_path = os.path.join(script_dir, "swap_count.pdf")

    plt.savefig(save_path, bbox_inches="tight")
