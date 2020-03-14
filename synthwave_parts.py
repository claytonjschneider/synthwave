import numpy as np
import matplotlib.cm as cm
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random
import itertools

def make_sun(ax, cx, cy, r):
    def make_grad(cx, cy, r, alpha):
        circ = mpatches.Circle((cx, cy), r, facecolor='none')
        ax.add_patch(circ)

        plt.imshow([[1, 1], [0, 0]],
            cmap=cm.plasma,
            interpolation='bicubic',
            aspect='auto',
            extent=(cx-r, cx+r, cy-r, cy+r),
            alpha=alpha,
            clip_path=circ,
            clip_on=True)

    make_grad(cx, cy, r+.2, alpha=.4)
    make_grad(cx, cy, r+.4, alpha=.4)
    make_grad(cx, cy, r+.8, alpha=.4)
    make_grad(cx, cy, r+.16, alpha=.4)
    make_grad(cx, cy, r, alpha=1)

    ax.plot([cx-r, cx+r], [cy-(r*0.8), cy-(r*0.8)],
        linewidth=r*.4, color='k')

    ax.plot([cx-r, cx+r], [cy-(r*0.6), cy-(r*0.6)],
        linewidth=r*.3, color='k')

    ax.plot([cx-r, cx+r], [cy-(r*0.4), cy-(r*0.4)],
        linewidth=r*.2, color='k')

    ax.plot([cx-r, cx+r], [cy-(r*0.2), cy-(r*0.2)],
        linewidth=r*.1, color='k')

def make_sun_reflection(ax, cx, cy, r):
    def make_grad(cx, cy, r, alpha):
        circ = mpatches.Circle((cx, cy), r, facecolor='none', zorder=1)
        ax.add_patch(circ)

        plt.imshow([[1, 1], [0, 0]],
            cmap=cm.plasma_r,
            interpolation='bicubic',
            aspect='auto',
            extent=(cx-r, cx+r, cy-r, cy+r),
            alpha=alpha,
            clip_path=circ,
            clip_on=True)

    make_grad(cx, -cy, r+.2, alpha=.2)
    make_grad(cx, -cy, r+.4, alpha=.2)
    make_grad(cx, -cy, r+.8, alpha=.2)
    make_grad(cx, -cy, r+.16, alpha=.2)
    make_grad(cx, -cy, r, alpha=.4)

    ax.plot([cx-r, cx+r], [-cy+(r*0.8), -cy+(r*0.8)],
        linewidth=r*.4, color='k')

    ax.plot([cx-r, cx+r], [-cy+(r*0.6), -cy+(r*0.6)],
        linewidth=r*.3, color='k')

    ax.plot([cx-r, cx+r], [-cy+(r*0.4), -cy+(r*0.4)],
        linewidth=r*.2, color='k')

    ax.plot([cx-r, cx+r], [-cy+(r*0.2), -cy+(r*0.2)],
        linewidth=r*.1, color='k')

def make_skyline(ax, min_x, max_x, min_y, max_y, towers=30, color='k', heights=None, widths=None):
    if heights is None:
        heights = np.random.randint(0, max_y-min_y, towers)

    x = np.linspace(min_x, max_x, towers)

    width = (max_x/towers)*2

    if widths is None:
        widths = [random.randint(0, 2) for i in range(towers)]
        widths = [a-1+width for a in widths]

    ax.bar(x, height=heights, width=widths, align='edge', bottom=min_y, color=color)

    return heights, widths

def make_skyline_reflection(ax, min_x, max_x, min_y, max_y, towers=30, color='k', heights=None, widths=None):
    if heights is None:
        heights = np.random.randint(0, max_y-min_y, towers)

    x = np.linspace(min_x, max_x, towers)

    width = (max_x/towers)*2

    if widths is None:
        widths = [random.randint(0, 2) for i in range(towers)]
        widths = [a-1+width for a in widths]

    ax.bar(x, height=-heights, width=widths, align='edge', bottom=min_y, color=color)


def make_stars(ax, min_x, max_x, min_y, max_y, stars=100):
    x = np.random.uniform(min_x, max_x, stars)
    y = np.random.uniform(min_y, max_y, stars)
    alpha_multiplier = np.random.uniform(.5, 1, len(x))
    size = np.random.uniform(1, 6, len(x))

    for i in range(len(y)):
        # calculate relative height
        h = (y[i] - min_y) / (max_y - min_y)

        ax.scatter(x[i], y[i], alpha=h*alpha_multiplier[i]*.1, s=1, c='#ffffff', zorder=0)
        ax.scatter(x[i], y[i], alpha=h*alpha_multiplier[i]*.1, s=1, c='#ffffff', zorder=0)
        ax.scatter(x[i], y[i], alpha=h*alpha_multiplier[i]*.1, s=1, c='#ffffff', zorder=0)
        ax.scatter(x[i], y[i], alpha=h*alpha_multiplier[i]*.1, s=1, c='#ffffff', zorder=0)
        ax.scatter(x[i], y[i], alpha=h*alpha_multiplier[i]*.6, s=1, c='#ffffff', zorder=0)
    return np.array([x, y, alpha_multiplier, size]).T
