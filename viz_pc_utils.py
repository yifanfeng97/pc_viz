from . import get_norm_heatmap_from_prob, get_heatmap_from_prob

from math import isnan
import numpy as np
import matplotlib.pyplot as plt
import bisect
from mpl_toolkits.mplot3d import Axes3D


def draw_pc(pc, show=True, save_dir=None):
    ax = plt.figure().add_subplot(111, projection='3d')
    ax.scatter(pc[:, 0], pc[:, 1], pc[:, 2])
    if show:
        plt.show()
    if save_dir is not None:
        plt.savefig(save_dir)


def vis(pc, mask, save_name, show=False):
    # color = heat_map_fun.get_heatmap_from_prob(mask)
    color = get_norm_heatmap_from_prob(mask)
    ax = plt.figure().add_subplot(111, projection='3d')
    ax.scatter(pc[:, 0], pc[:, 1], pc[:, 2], c=color)

    # airplane
    l_val = 0.5
    offset_x = 0.4
    offset_y = 0
    offset_z = 0.4

    ax.set_xlim(-l_val+offset_x, l_val+offset_x)
    ax.set_ylim(-l_val+offset_y, l_val+offset_y)
    ax.set_zlim(-l_val+offset_z, l_val+offset_z)
    ax.axis('off')
    if show:
        plt.show()
    else:
        plt.savefig(save_name)


if __name__ == '__main__':
    pass
