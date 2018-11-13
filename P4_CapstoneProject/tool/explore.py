#!/user/bin/env python
#-*-coding:utf-8-*-

from matplotlib import pyplot as plt
import matplotlib as mtl
import numpy as np

def missing_value_plot(
    data, title, figsize=(12,15), color="grey", facecolor="honeydew", ylabel="",
    xlabel="", title_loc="left", fontsize=20, pad=20.0, ticklocation:dict=None
    ):
    """Plot the missing value information
    Plot the missing value about the specific labels

    Parameters:
    data: DataFrame
        It is the missing value statistic information about the labels 
    title, ylabel, xlabel: string
        Those are the information about the title, the x axis and the y axis 
    figsize: tuple
        It is the figure size
    color: string or matplotlib color infor
        It is the artist color
    facecolor: string or matplotli color infor
        It is the axes color that is backgroung color about the artist
    title_loc: string
        Which title to set, default to left
    fontsize: int
        Control the appearance of the text about the title and the label
    pad: float
        The offset of the title from the top of the axes
    ticklocation: dict
        Control the the axis tick location. The key is location, and the value is
        boolean that can control the ticklocation

    Results:
    ax: Axes object
        It is the plot Axes object, which can adjust the plot
    """
    plt.figure(figsize=figsize)
    ax = plt.subplot()
    ax.set_facecolor(facecolor)
    data.plot(kind="barh", ax=ax, color=color)

    ax.set_title(title, fontsize=fontsize, loc=title_loc, pad=pad)
    ax.set_ylabel(ylabel, fontsize=fontsize*0.8)
    ax.set_xlabel(xlabel, fontsize=fontsize*0.8)

    # set the ticklabel
    ax.tick_params(**ticklocation)

    return ax