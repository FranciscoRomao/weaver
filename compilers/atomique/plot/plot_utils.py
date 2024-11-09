import os

import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.ticker as mticker
import numpy as np
import yaml
from matplotlib import cm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from scipy.stats.mstats import gmean

plt.rcParams["hatch.linewidth"] = 2
plt.rcParams["font.family"] = "Liberation Sans"

plt.rcParams["hatch.linewidth"] = 2
plt.rcParams["font.family"] = "Liberation Sans"


patterns = ["+", "\\" * 3, "O", "///", "*", "-", "|", "*", "o", "O", None]

colors = ["#F8B62D", "#00AEBB", "#A31F34", "#0081CC", "#8A8B8C", "#70ae47"]

color_dict = {
    "Superconducting": "#0081CC",
    "Baker-Long-Range": "#8A8B8C",
    "FPQA-C": "#A31F34",
    "FPQA-C-Generic": "#0081CC",
    "FPQA-C-Flying": "#A31F34",
    "FAA-Triangular": "#00AEBB",
    "FAA-Rectangular": "#F8B62D",
    "Tan-Heuristic": "#F8B62D",
    "Tan-Solver": "#0081CC",
}

pattern_dict = {
    "Superconducting": ".",
    "Baker-Long-Range": "+",
    "FPQA-C": "///",
    "FPQA-C-Generic": "///",
    "FPQA-C-Flying": "\\" * 3,
    "FAA-Triangular": "\\" * 3,
    "FAA-Rectangular": "O",
    "Tan-Heuristic": "\\" * 3,
    "Tan-Solver": "O",
}


shape_dict = {
    "FAA-Rectangular": "-+",
    "FAA-Triangular": "-o",
    "FPQA-C": "-*",
    "FPQA-C-Generic": "-*",
    "FPQA-C-Flying": "-o",
    "Tan-Heuristic": "-+",
    "Tan-Solver": "-o",
}


def CustomCmap(from_rgb, to_rgb):
    # from color r,g,b
    r1, g1, b1 = from_rgb

    # to color r,g,b
    r2, g2, b2 = to_rgb

    cdict = {
        "red": ((0, r1, r1), (1, r2, r2)),
        "green": ((0, g1, g1), (1, g2, g2)),
        "blue": ((0, b1, b1), (1, b2, b2)),
    }

    cmap = mpl.colors.LinearSegmentedColormap("custom_cmap", cdict)
    return cmap


red_cmap = CustomCmap(
    (217 / 255, 163 / 255, 174 / 255), (163 / 255, 31 / 255, 52 / 255)
)
green_cmap = CustomCmap(
    (157 / 255, 222 / 255, 227 / 255), (0 / 255, 174 / 255, 187 / 255)
)
yellow_cmap = CustomCmap(
    (252 / 255, 226 / 255, 176 / 255), (248 / 255, 182 / 255, 45 / 255)
)


cmap_dict = {
    "FPQA-C": red_cmap,
    "flying": red_cmap,
    "FAA-Triangular": green_cmap,
    "FAA-Rectangular": yellow_cmap,
}

import io

from matplotlib import _tight_bbox as tight_bbox
from matplotlib.transforms import Affine2D, Bbox, TransformedBbox


def tight_figure(fig, **kwargs):
    # canvas = fig.canvas._get_output_canvas(None, 'png')
    canvas = fig.canvas
    print_method = getattr(canvas, "print_png")
    print_method(io.BytesIO())
    renderer = fig._cachedRenderer
    bbox_inches = fig.get_tightbbox(renderer)

    bbox_artists = fig.get_default_bbox_extra_artists()

    bbox_filtered = []
    for a in bbox_artists:
        bbox = a.get_window_extent(renderer)
        if a.get_clip_on():
            clip_box = a.get_clip_box()
            if clip_box is not None:
                bbox = Bbox.intersection(bbox, clip_box)
            clip_path = a.get_clip_path()
            if clip_path is not None and bbox is not None:
                clip_path = clip_path.get_fully_transformed_path()
                bbox = Bbox.intersection(bbox, clip_path.get_extents())
        if bbox is not None and (bbox.width != 0 or bbox.height != 0):
            bbox_filtered.append(bbox)

    if bbox_filtered:
        _bbox = Bbox.union(bbox_filtered)
        trans = Affine2D().scale(1.0 / fig.dpi)
        bbox_extra = TransformedBbox(_bbox, trans)
        bbox_inches = Bbox.union([bbox_inches, bbox_extra])

    pad = kwargs.pop("pad_inches", None)
    if pad is None:
        pad = plt.rcParams["savefig.pad_inches"]

    bbox_inches = bbox_inches.padded(pad)

    tight_bbox.adjust_bbox(fig, bbox_inches, canvas.fixed_dpi)

    w = bbox_inches.x1 - bbox_inches.x0
    h = bbox_inches.y1 - bbox_inches.y0
    fig.set_size_inches(w, h)


def autolabel(ax, rects, fontsize=10, keep_digits=2, rotation=25):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        if keep_digits == 0:
            text = ax.annotate(
                "{:.0f}".format(height) if height < 10 else "{:.0f}".format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=fontsize,
            )
        elif keep_digits == 1:
            text = ax.annotate(
                "{:.1f}".format(height) if height < 10 else "{:.0f}".format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=fontsize,
            )
        elif keep_digits == 2:
            text = ax.annotate(
                "{:.2f}".format(height) if height < 10 else "{:.0f}".format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=fontsize,
            )
        elif keep_digits == 3:
            text = ax.annotate(
                "{:.3f}".format(height) if height < 10 else "{:.0f}".format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=fontsize,
            )
        elif keep_digits == 4:
            text = ax.annotate(
                "{:.4f}".format(height) if height < 10 else "{:.0f}".format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=fontsize,
            )
        text.set_rotation(rotation)


def plot_improvements(
    ax,
    benchmarks,
    baselines,
    hardwares,
    improvements,
    ylabel,
    fname=None,
    figsize=(15, 5),
    colors=colors,
    patterns=patterns,
    width_scale=1.0,
    xticklabels_configs=dict(),
    ylog=False,
    yticks=None,
    ylim=None,
    ylabel_configs=dict(),
    legend_configs=dict(),
    plot_legend=False,
    geo_mean=False,
    keep_digits=2,
    plot_xticks=False,
    ncol=None,
    rotation=25,
):
    _xticklabels_configs = dict(
        fontsize=10, rotation=25, ha="center", multialignment="right"
    )
    _xticklabels_configs.update(xticklabels_configs)
    _ylabel_configs = dict(fontsize=12)
    _ylabel_configs.update(ylabel_configs)
    _legend_configs = dict(columnspacing=0.7, fontsize=12)
    _legend_configs.update(legend_configs)

    num_benchmarks = len(benchmarks) + 1
    num_baselines = len(baselines)
    num_hardwares = len(hardwares)
    num_groups = num_baselines * num_hardwares

    x = np.arange(num_benchmarks)
    offsets = np.arange(0, 2, 2 / num_groups) - (num_groups - 1) / num_groups
    group_width = 0.4 * width_scale
    width = 2 * group_width / num_groups

    # fig, ax = plt.subplots(figsize=figsize)
    rects = []
    for hardware_id, (hardware, hardware_name) in hardwares.items():
        for baseline_id, (baseline, baseline_name) in baselines.items():
            # for baseline_id in ids:
            baseline_id = str(baseline_id)
            baseline, baseline_name = baselines[str(baseline_id)]
            group_id = int(hardware_id) * num_baselines + int(baseline_id)
            data = []
            for benchmark_id in benchmarks.keys():
                data.append(improvements[eval(baseline_id)][eval(benchmark_id)])
            data.append(gmean(data) if geo_mean else np.mean(data))
            rects.append(
                ax.bar(
                    x + group_width * offsets[group_id],
                    data,
                    width,
                    label=(
                        baseline_name
                        if num_hardwares == 1
                        else f"{hardware_name} / {baseline_name}"
                    ),
                    align="center",
                    hatch=patterns[int(baseline_id)],
                    edgecolor="white",
                    color=colors[group_id if num_hardwares == 1 else int(hardware_id)],
                )
            )
            # just for box
            ax.bar(
                x + group_width * offsets[group_id],
                data,
                width,
                align="center",
                edgecolor="black",
                color="none",
            )

    for r in rects:
        autolabel(
            ax,
            r,
            fontsize=_legend_configs["fontsize"] - 5,
            keep_digits=keep_digits,
            rotation=rotation,
        )
    if plot_legend:
        ax.legend(
            loc="lower center",
            bbox_to_anchor=(0.45, 1.1),
            ncol=len(baselines) if ncol is None else ncol,
            **_legend_configs,
        )

    # Y-axis
    if ylim is not None:
        ax.set_ylim(ylim)
    if ylog:
        ax.set_yscale("log")
    elif yticks is not None:
        ax.set_yticks(yticks)
    ax.set_ylabel(ylabel, **_ylabel_configs)
    ax.tick_params(axis="y", labelsize=_ylabel_configs["fontsize"] - 2)
    # X-axis
    if plot_xticks:
        ax.set_xticks(x)
        ax.set_xticklabels(
            [benchmark_name for _, benchmark_name in benchmarks.values()]
            + ["GMean" if geo_mean else "Mean"],
            **_xticklabels_configs,
        )
        ax.xaxis.set_tick_params(pad=-2)
    else:
        ax.set_xticks(x)
        ax.set_xticklabels([])

    ax.margins(0.02, 0.02)
    ax.grid(axis="y", alpha=0.5, linestyle="--")

    if fname is not None:
        plt.savefig(
            f"{fname}.pdf",
            transparent=True,
            bbox_inches="tight",
            format="pdf",
            pad_inches=0.025,
        )

    # tight_figure(fig)
    # plt.savefig('bar.pdf')


def plot_bars(
    ax,
    orig_data=None,
    compilers=["sc", "baker", "faa", "geyser", "fpqac"],
    compiler_names=[
        "Superconducting",
        "Baker-Long-Range",
        "FAA-Rectangular",
        "FAA-Triangular",
        "FPQA-C",
    ],
    benchs=[
        "HHL-7",
        "Mermin-Bell-10",
        "QV-32",
        "BV-50",
        "BV-70",
        "QSim-rand-20",
        "QSim-rand-40",
        "QSim-rand-20-p0.3",
        "QSim-rand-40-p0.3",
        "H2-4",
        "LiH-8",
        "QAOA-rand-10",
        "QAOA-rand-20",
        "QAOA-rand-30",
        "QAOA-rand-50",
        "QAOA-regu5-40",
        "QAOA-regu6-100",
    ],
    paths=["13_isca_maintable/arb", "13_isca_maintable/qsim", "13_isca_maintable/qaoa"],
    y_first_level_name="fidelity",
    y_second_level_name="total_fidelity",
    is_y_log=False,
    y_label="Fidelity",
    plot_legend=False,
    y_lim=None,
    geo_mean=False,
    keep_digits=2,
    plot_xticks=False,
    rotation=25,
):
    res_dict = {}

    if orig_data is None:
        # retrieve data
        data = []
        for compiler in compilers:
            res_dict[compiler] = []
            for path in paths:
                file_path = os.path.join(f"results/", path, f"{compiler}/res.yml")
                print(file_path)
                with open(file_path, "r") as file:
                    res_list = yaml.load(file, Loader=yaml.FullLoader)
                    res_dict[compiler].extend(res_list)

        for compiler in compilers:
            for info in res_dict[compiler]:
                if y_second_level_name is None:
                    this_data = info[y_first_level_name]
                    if type(this_data) == str:
                        this_data = eval(this_data)
                    data.append(this_data)
                else:
                    this_data = info[y_first_level_name][y_second_level_name]
                    if type(this_data) == str:
                        this_data = eval(this_data)
                    data.append(this_data)

        # print(len(data))
        data = np.array(data).reshape((len(compilers), -1))
    else:
        data = np.array(orig_data)
    print(data.T)
    benchmarks = {}

    for k, benchmark in enumerate(benchs):
        benchmarks[str(k)] = ("", benchmark)

    baselines = {}
    for k, compiler in enumerate(compilers):
        baselines[str(k)] = ("", compiler_names[k])

    colors = [color_dict[compiler_name] for compiler_name in compiler_names]
    patterns = [pattern_dict[compiler_name] for compiler_name in compiler_names]
    print(data.shape)

    plot_improvements(
        ax,
        benchmarks=benchmarks,
        baselines=baselines,
        hardwares={"0": ("0", "0")},
        improvements=data,
        ylabel=y_label,
        colors=colors,
        patterns=patterns,
        ylog=is_y_log,
        plot_legend=plot_legend,
        ylim=y_lim,
        geo_mean=geo_mean,
        keep_digits=keep_digits,
        plot_xticks=plot_xticks,
        rotation=rotation,
    )


def plot_2d_breakdown_fill(
    ax,
    compiler="fpqac",
    path="results/ablation/T_per_move/arb",
    x_first_level_name="hyperparams",
    x_second_level_name="T_per_move",
    breakdown_parts_first_level_name="fidelity",
    breakdown_parts_second_level_name=[
        "1q_total",
        "2q_total",
        "additional_2Q_error_by_heating",
        "additional_2Q_by_cooling",
        "movement_atomloss",
        "movement_decoherence",
    ],
    breakdown_name=["1Q", "2Q", "Heating", "Cooling", "Atom Loss", "Move Decoherence"],
    is_x_log=False,
    is_y_log=False,
    bench="BV70",
    compiler_name="FPQA-C",
    xlabel="Time per move (us)",
    ylabel="Fidelity",
    xlim=None,
    ylim=None,
    ylim_inset=None,
    inset_loc=1,
    inset_size=["30%", "30%"],
    plot_legend=False,
    x_scale=1,
    xbins=5,
    special_x_log=False,
):
    res_y = {}
    variable = []

    # retrieve data
    file_path = os.path.join(path, f"{compiler}/res.yml")
    print(file_path)
    with open(file_path, "r") as file:
        res_list = yaml.load(file, Loader=yaml.FullLoader)

    for info in res_list:
        variable.append(info[x_first_level_name][x_second_level_name])
        for name in breakdown_parts_second_level_name:
            if name not in res_y.keys():
                res_y[name] = []
            res_y[name].append(info[breakdown_parts_first_level_name][name])
    res_y_array = np.array([res_y[name] for name in breakdown_parts_second_level_name])

    res_y_log = -np.log(res_y_array)

    infidelity = 1 - res_y_array
    res_y_infidelity_contri = infidelity * (res_y_log / np.sum(res_y_log, axis=0))
    # print(res_y_infidelity_contri)
    # print(res_y_log)

    if type(variable[0]) == str:
        variable = list(map(lambda x: eval(x), variable))

    variable = np.array(variable) / x_scale
    x_start = min(variable)
    x_end = max(variable)
    # X = np.arange(len(variable))

    res_y_plot = res_y_log
    res_log_previous = np.zeros_like(res_y_plot[0])
    res_log_cumu = np.zeros_like(res_y_plot[0])
    axins = inset_axes(
        ax,
        width=inset_size[0],
        height=inset_size[1],
        loc=inset_loc,
        borderpad=2 if inset_loc == 2 else 1,
    )

    if not special_x_log:
        if is_x_log:
            ax.set_xscale("log")
            axins.set_xscale("log")
        else:
            ax.set_xscale("linear")
            ax.locator_params(axis="x", nbins=xbins)
            axins.locator_params(axis="x", nbins=xbins)

    else:
        ax.set_xscale("log")
        ax.invert_xaxis()
        axins.set_xscale("log")
        axins.invert_xaxis()

        variable = 1 - variable

    if is_y_log:
        ax.set_yscale("log")
    else:
        ax.set_yscale("linear")

    for i, increment in enumerate(res_y_plot):
        res_log_cumu += increment
        # print(res_log_cumu)
        ax.plot(variable, res_log_cumu, color="k", linewidth=0.5)
        axins.plot(variable, res_log_cumu, color="k", linewidth=0.5)
        ax.fill_between(
            variable,
            res_log_previous,
            res_log_cumu,
            color=colors[i],
            label=breakdown_name[i],
            hatch=patterns[i],
            edgecolor="white",
            linewidth=0.3,
            alpha=0.7,
        )
        axins.fill_between(
            variable,
            res_log_previous,
            res_log_cumu,
            color=colors[i],
            label=breakdown_name[i],
            hatch=patterns[i],
            edgecolor="white",
            linewidth=0.3,
            alpha=0.7,
        )
        res_log_previous = res_log_cumu.copy()

    if plot_legend:
        ax.legend(
            bbox_to_anchor=(0, 1.02, 1, 0.2),
            loc="lower left",
            borderaxespad=0,
            ncol=6,
            fontsize=15,
        )

    if xlim is not None:
        ax.set_xlim(xlim)
    else:
        print(x_start, x_end)
        if not special_x_log:
            ax.set_xlim([x_start, x_end])
            axins.set_xlim([x_start, x_end])

    if special_x_log:
        ax.set_xticklabels(1 - ax.get_xticks())
        axins.set_xticklabels(1 - axins.get_xticks())

    if ylim is not None:
        ax.set_ylim(ylim)

    if ylim_inset is not None:
        axins.set_ylim(ylim_inset)

    if x_second_level_name == "avg_move_speed":
        axins.set_xticks([0.02, 0.08])

    if x_second_level_name == "T_per_move":
        axins.set_xticks([200, 600, 1000])

    # axins.set_xticklabels(ax.get_xticks(), fontsize=10)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # ax.set_title(f"{compiler_name} Fidelity Breakdown for {bench}")

    # print(variable)
    # print(res_y)

    # 1q_decoherence: 0.9997708595900231
    # 1q_gate: 0.9669569109151244
    # 2q_decoherence: 0.9999331222364269
    # 2q_gate: 0.548399494893968
    # additional_2Q_by_cooling: 0.895710760918251
    # additional_2Q_error_by_heating: 0.8121728314181023
    # movement_atomloss: 0.9956790519512018
    # movement_decoherence: 0.9825539753546094
    # total_fidelity: 0.37728334412298414
    # transfer: 1.0
    # transfer_decoherence: 1.0


def plot_2d_curve(
    ax,
    n_series=3,
    compilers=["faa", "geyser", "fpqac"],
    paths=[
        "results/ablation/T_per_move/arb",
        "results/ablation/T_per_move/qsim",
        "results/ablation/T_per_move/qaoa",
    ],
    x_first_level_name="hyperparams",
    x_second_level_name="T_per_move",
    y_first_level_name="fidelity",
    y_second_level_name="total_fidelity",
    is_x_log=False,
    is_y_log=False,
    benchs=["BV70", "QSim-rand-20", "QAOA-regu5-40"],
    compiler_names=["FAA-Rectangular", "FAA-Triangular", "FPQA-C"],
    xlabel="Time per move (us)",
    ylabel="Fidelity",
    xlim=None,
    ylim=None,
    plot_legend=False,
    x_scale=1,
    xbins=5,
    special_x_log=False,
    is_catogorical=False,
    xticks=None,
):
    res_y = {}
    res_dict = {}
    variable = []

    # retrieve data
    for compiler in compilers:
        res_dict[compiler] = []
        for path in paths:
            file_path = os.path.join(path, f"{compiler}/res.yml")
            print(file_path)
            with open(file_path, "r") as file:
                res_list = yaml.load(file, Loader=yaml.FullLoader)
                res_dict[compiler].extend(res_list)

    for compiler in compilers:
        for info in res_dict[compiler]:
            if compiler not in res_y.keys():
                res_y[compiler] = []
            res_y[compiler].append(info[y_first_level_name][y_second_level_name])
            if compiler == "fpqac":
                this_data = info[x_first_level_name][x_second_level_name]
                if type(this_data) == str:
                    this_data = eval(this_data)
                if type(this_data) == list:
                    this_data = this_data[0]
                variable.append(this_data)
    if type(variable[0]) == str:
        variable = list(map(lambda x: eval(x), variable))
    variable = np.array(variable) / x_scale
    x_start = min(variable)
    x_end = max(variable)

    assert len(variable) % n_series == 0
    n_points = int(len(variable) // n_series)

    for compiler in compilers:
        res_y[compiler] = np.array(res_y[compiler]).reshape((n_series, n_points))
        variable = np.array(variable).reshape((n_series, n_points))
    # z_min = min([res_y[compiler].flatten().min() for compiler in compilers])
    # z_max = max([res_y[compiler].flatten().max() for compiler in compilers])

    if not special_x_log:
        if is_x_log:
            ax.set_xscale("log")
        else:
            ax.set_xscale("linear")
            ax.locator_params(
                axis="x", nbins=xbins if not is_catogorical else len(xticks)
            )
    else:
        ax.set_xscale("log")
        ax.invert_xaxis()
        variable = 1 - variable

    if is_y_log:
        ax.set_yscale("log")
    else:
        ax.set_yscale("linear")

    # x = np.linspace(x_start, x_end, n_points)
    shapes = [
        "-+",
        "-o",
        "-*",
        "-^",
        "-s",
        "-D",
        "-X",
        "-P",
        "-v",
        "-H",
        "-d",
        "-p",
        "-|",
        "-_",
        "-<",
        "->",
        "-1",
        "-2",
        "-3",
        "-4",
        "-8",
        "-s",
        "-p",
        "-*",
    ]
    for i in range(n_series):
        for k, compiler in enumerate(compilers):
            # y = np.ones(x.size) * i
            # ax.plot(variable[i], res_y[compiler][i], shapes[i], color=color_dict[compiler_names[k]], label=f"{benchs[i]}-{compiler_names[k]}")
            print(y_second_level_name)
            if y_second_level_name == "avg_move_distance":
                res_y[compiler][i] *= 1000
            if is_catogorical:
                ax.plot(
                    np.arange(len(variable[i])),
                    res_y[compiler][i],
                    shape_dict[compiler_names[k]],
                    color=colors[i],
                    label=f"{benchs[i]}",
                )
            else:
                ax.plot(
                    variable[i],
                    res_y[compiler][i],
                    shape_dict[compiler_names[k]],
                    color=colors[i],
                    label=f"{benchs[i]}-{compiler_names[k]}",
                )
            # plt.yscale("log")
            # ax.add_collection3d(plt.fill_between(x, z_min, z_max, color='grey', alpha=0.05), zs=i, zdir='y')

    if special_x_log:
        ax.set_xticklabels(1 - ax.get_xticks())
    elif xticks is not None:
        ax.set_xticklabels(
            xticks, fontsize=10, rotation=270, ha="center", multialignment="right"
        )
        ax.set_xlim([0, len(xticks) - 1])

    if plot_legend:
        ax.legend(
            bbox_to_anchor=(0, 1.02, 1, 0.2),
            loc="lower left",
            borderaxespad=0,
            ncol=n_series,
            fontsize=13,
        )

    if xlim is not None:
        ax.set_xlim(xlim)
    else:
        if not special_x_log and not is_catogorical:
            ax.set_xlim([x_start, x_end])
        # ax.set_xlim([x_start, x_end])

    if ylim is not None:
        ax.set_ylim(ylim)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # os.makedirs(os.path.join(f'plot/', path, f'{x_second_level_name}'), exist_ok=True)
    # save_path = os.path.join(f'plot/', path, f'{x_second_level_name}/2dplot.pdf')
    # plt.savefig(save_path)


def plot_surface(
    fig,
    ax,
    nq=40,
    X=np.array([2, 6, 10, 14, 18, 22, 26]),
    Y=np.array([1, 2, 3, 4, 5, 6, 7]),
    repeat=3,
    compilers=["geyser", "fpqac_generic"],
    compiler_names=["FAA-Triangular", "FPQA-C"],
    path="results/arb/surf_comp_maxd10/",
    z_first_level_name="fidelity",
    z_second_level_name="total_fidelity",
    is_plot_ratio=False,
    alphas=[0.75, 1],
    xlabel="2Q gate per Q",
    ylabel="Interation per Q",
    zlabel="Fidelity Improv.",
    is_z_log=False,
    is_fake_reverse=False,
    use_log=True,
    # cbar_loc=[[0.13, 0.5, 0.02, 0.2], [0.25, 0.5, 0.02, 0.2]]
):
    ax.set_proj_type("ortho")
    res_Z = {}
    res_n2q = {}
    res_dict = {}
    linew = 1

    for compiler in compilers:
        file_path = os.path.join(f"{path}", f"{compiler}/res.yml")
        print(file_path)
        with open(file_path, "r") as file:
            res_list = yaml.load(file, Loader=yaml.FullLoader)
            res_dict[compiler] = res_list

    for compiler in compilers:
        for info in res_dict[compiler]:
            if compiler not in res_Z.keys():
                res_Z[compiler] = []
                res_n2q[compiler] = []
            res_Z[compiler].append(info[z_first_level_name][z_second_level_name])

        # perform average
        res_Z[compiler] = [
            (sum(res_Z[compiler][i : i + repeat]) / repeat)
            for i in range(0, len(res_Z[compiler]), repeat)
            if i + repeat - 1 < len(res_Z[compiler])
        ]

    X, Y = np.meshgrid(X, Y)

    # Z0 = res_Z[compilers[0]]
    # Z0 = np.array(Z0).reshape((X.shape[0], Y.shape[0])).transpose()
    # Z1 = res_Z[compilers[1]]
    # Z1 = np.array(Z1).reshape((X.shape[0], Y.shape[0])).transpose()
    # print(Z0-Z1)

    if is_plot_ratio:
        Z0 = res_Z[compilers[0]]
        Z0 = np.array(Z0).reshape((X.shape[1], X.shape[0])).transpose()
        Z1 = res_Z[compilers[1]]
        Z1 = np.array(Z1).reshape((X.shape[1], X.shape[0])).transpose()
        Z = np.array(Z1) / np.array(Z0)
        if use_log:
            Z = np.log10(Z)
        surf = ax.plot_surface(
            X, Y, Z, cmap=cm.coolwarm, linewidth=linew, antialiased=False, alpha=0.5
        )
        levels_x = X.tolist()[0]
        levels_x[-1] -= 0.01

        levels_y = Y[:, 0].tolist()
        levels_y[-1] -= 0.01

        ax.set(
            ylim=(Y.min(), Y.max()),
            xlim=(X.min(), X.max()),
            zlim=((Z).flatten().min(), (Z).flatten().max()),
        )

        def log_tick_formatter(val, pos=None):
            return f"$10^{{{int(val)}}}$"

        if use_log:
            ax.zaxis.set_major_formatter(mticker.FuncFormatter(log_tick_formatter))
            ax.zaxis.set_major_locator(mticker.MaxNLocator(integer=True))
        ax.contour(X, Y, Z, zdir="x", offset=X[0][0], cmap="copper", levels=levels_x)
        ax.contour(X, Y, Z, zdir="y", offset=Y[-1][-1], cmap="copper", levels=levels_y)
        # ax.title.set_text(f"Fidelity Improvement, N_Q={nq}")

    else:
        if is_fake_reverse:
            itms = reversed(res_Z.items())
        else:
            itms = res_Z.items()

        for k, (compiler, Z) in enumerate(itms):
            if is_fake_reverse:
                k = len(compilers) - k - 1
            Z = np.array(Z).reshape((X.shape[1], X.shape[0])).transpose()
            # print(Z)

            surf = ax.plot_surface(
                X,
                Y,
                Z,
                cmap=cmap_dict[compiler_names[k]],
                linewidth=linew,
                antialiased=False,
                alpha=alphas[k],
            )

            ax.plot_wireframe(X, Y, Z, color="black", linewidth=0.1, alpha=alphas[k])
            # cbar = fig.colorbar(surf)
            # cbar.locator = mpl.ticker.MaxNLocator(nbins=6)
            # cbar.ax.set_position(cbar_loc[k])
        # ax.title.set_text(f"2Q Gate Comparison, N_Q={nq}")

    if is_z_log:
        ax.set_zscale("log")

    ax.set_xticks(X.tolist()[0])
    ax.set_yticks(Y[:, 0].tolist())
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_zlabel(zlabel)


def plot_bars_SWAP(
    ax,
    orig_data=None,
    compilers=["sc", "baker", "faa", "geyser", "fpqac"],
    compiler_names=[
        "Superconducting",
        "Baker-Long-Range",
        "FAA-Rectangular",
        "FAA-Triangular",
        "FPQA-C",
    ],
    benchs=[
        "HHL-7",
        "Mermin-Bell-10",
        "QV-32",
        "BV-50",
        "BV-70",
        "QSim-rand-20",
        "QSim-rand-40",
        "H2-4",
        "LiH-8",
        "QAOA-rand-10",
        "QAOA-rand-20",
        "QAOA-regu5-40",
        "QAOA-regu6-100",
    ],
    paths=["25_swap_count/arb", "25_swap_count/qsim", "25_swap_count/qaoa"],
    y_first_level_name="fidelity",
    y_second_level_name="total_fidelity",
    is_y_log=False,
    y_label="Fidelity",
    plot_legend=False,
    y_lim=None,
    geo_mean=False,
    keep_digits=2,
    plot_xticks=False,
):
    res_dict = {}
    original_2q = []
    if orig_data is None:
        # retrieve data
        data = []
        for compiler in compilers:
            res_dict[compiler] = []
            for path in paths:
                file_path = os.path.join(f"results/", path, f"{compiler}/res.yml")
                print(file_path)
                with open(file_path, "r") as file:
                    res_list = yaml.load(file, Loader=yaml.FullLoader)
                    res_dict[compiler].extend(res_list)

        for compiler in compilers:
            for info in res_dict[compiler]:
                if y_second_level_name is None:
                    data.append(info[y_first_level_name])
                else:
                    print(info)
                    data.append(info[y_first_level_name][y_second_level_name])
        for info in res_dict["fpqac"]:
            # print(info)
            original_2q.append(info["others"]["original_n_2q_gates"])

        # print(len(data))
        data = np.array(data).reshape((len(compilers), -1)) - np.array(original_2q)
    else:
        data = np.array(orig_data)
    print(data.T)
    benchmarks = {}

    for k, benchmark in enumerate(benchs):
        benchmarks[str(k)] = ("", benchmark)

    baselines = {}
    for k, compiler in enumerate(compilers):
        baselines[str(k)] = ("", compiler_names[k])

    colors = [color_dict[compiler_name] for compiler_name in compiler_names]
    patterns = [pattern_dict[compiler_name] for compiler_name in compiler_names]
    print(data.shape)

    plot_improvements(
        ax,
        benchmarks=benchmarks,
        baselines=baselines,
        hardwares={"0": ("0", "0")},
        improvements=data,
        ylabel=y_label,
        colors=colors,
        patterns=patterns,
        ylog=is_y_log,
        plot_legend=plot_legend,
        ylim=y_lim,
        geo_mean=geo_mean,
        keep_digits=keep_digits,
        plot_xticks=plot_xticks,
        rotation=90,
    )
