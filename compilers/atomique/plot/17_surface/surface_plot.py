import os

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from plot.plot_utils import color_dict, plot_surface

if __name__ == "__main__":
    # import pdb
    # pdb.set_trace()
    fig, ax = plt.subplots(2, 2, subplot_kw={"projection": "3d"}, figsize=[9, 8])
    plt.subplots_adjust(wspace=0.1, hspace=0.1)

    nqs = [40]
    comp_names = ["FAA-Rectangular", "FAA-Triangular"]
    zlabels = ["Number of 2Q Gates", "Fidelity Improv."]
    for i, nq in enumerate(nqs):
        for k, comp in enumerate(["faa", "geyser"]):
            for j in range(2):
                plot_surface(
                    fig,
                    ax[j][i * 2 + k],
                    nq=nq,
                    X=np.array([10, 20, 40, 60, 80, 100]),
                    Y=np.array([1, 2, 3, 4, 5, 6, 7]),
                    repeat=3,
                    compilers=[comp, "fpqac_generic"],
                    compiler_names=[comp_names[k], "FPQA-C"],
                    path="results/17_surface/qaoa/",
                    z_first_level_name="circ_stats" if j == 0 else "fidelity",
                    z_second_level_name="n_2q_gate" if j == 0 else "total_fidelity",
                    is_plot_ratio=(j == 1),
                    alphas=[0.75, 0.75],
                    ylabel="Degree",
                    xlabel="Qubit Number",
                    zlabel=zlabels[j],
                    is_fake_reverse=False,
                )
    fake2Dline = mpl.lines.Line2D(
        [0], [0], linestyle="none", c=color_dict["FAA-Rectangular"], marker="s"
    )
    fake2Dline1 = mpl.lines.Line2D(
        [0], [0], linestyle="none", c=color_dict["FAA-Triangular"], marker="s"
    )
    fake2Dline2 = mpl.lines.Line2D(
        [0], [0], linestyle="none", c=color_dict["FPQA-C"], marker="s"
    )
    fig.legend(
        [fake2Dline, fake2Dline1, fake2Dline2],
        ["FAA-Rectangular", "FAA-Triangular", "FPQA-C"],
        numpoints=1,
        loc="upper left",
        bbox_to_anchor=[0.2, 0.89],
        ncol=3,
    )

    script_dir = os.path.dirname(__file__)

    save_path = os.path.join(script_dir, "3d_n2q_fid_qaoa.pdf")

    fig.savefig(save_path, bbox_inches="tight")
