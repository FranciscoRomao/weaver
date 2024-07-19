import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc("font", **{"size": 15})

if __name__ == "__main__":
    fig, axs = plt.subplots(1, 4, figsize=(11, 2))
    plt.subplots_adjust(wspace=0.3)
    length = 300
    t = np.arange(length + 1)

    jerk = -0.0000065

    initial_acceleration = np.abs(150 * jerk)

    axs[0].plot(t, jerk * np.ones(length + 1))
    axs[0].set_ylim([jerk * 2, -jerk * 2])
    axs[0].set_xlabel("Time ($\mu s$)")
    axs[0].set_xticks([0, 100, 200, 300])
    axs[0].set_ylabel("Jerk ($\mu m/\mu s^3$)")
    axs[0].yaxis.set_label_coords(0.15, 0.5, transform=None)

    axs[1].plot(t, jerk * t + initial_acceleration)
    # axs[1].set_ylim([-5, 5])
    axs[1].set_xlabel("Time ($\mu s$)")
    axs[1].set_xticks([0, 100, 200, 300])
    axs[1].set_ylabel("Accel. ($\mu m/\mu s^2$)")
    axs[1].yaxis.set_label_coords(0.15, 0.5, transform=None)

    axs[2].plot(t, jerk / 2 * t**2 + initial_acceleration * t)
    # axs[2].set_ylim([-5, 5])
    axs[2].set_xlabel("Time ($\mu s$)")
    axs[2].set_xticks([0, 100, 200, 300])
    axs[2].set_ylabel("Velo. ($\mu m/\mu s$)")
    axs[2].yaxis.set_label_coords(0.15, 0.5, transform=None)

    axs[3].plot(t, jerk / 2 / 3 * t**3 + initial_acceleration / 2 * t**2)
    # axs[3].set_ylim([-5, 5])
    axs[3].set_xlabel("Time ($\mu s$)")
    axs[3].set_xticks([0, 100, 200, 300])
    axs[3].set_ylabel("Distance ($um$)")
    axs[3].set_yticks([0, 5, 10, 15])
    axs[3].yaxis.set_label_coords(0.15, 0.5, transform=None)

    script_dir = os.path.dirname(__file__)

    save_path = os.path.join(script_dir, "move_pattern.pdf")

    fig.savefig(save_path, bbox_inches="tight")
