BLUE = "#1A85FF"
RED = "#D0021B"
METRIC_EPS = 1e-6

from matplotlib import rc


def plot_typography(
    usetex: bool = False, small: int = 16, medium: int = 20, big: int = 22
):
    """
    Initializes font settings and visualization backend (LaTeX or standard matplotlib).
    :param usetex: flag to indicate the usage of LaTeX (needs LaTeX indstalled)
    :param small: small font size in pt (for legends and axes' ticks)
    :param medium: medium font size in pt (for axes' labels)
    :param big: big font size in pt (for titles)
    :return:
    """

    # font family
    rc("font", **{"family": "sans-serif", "sans-serif": ["Helvetica"]})
    ## for Palatino and other serif fonts use:
    # rc('font',**{'family':'serif','serif':['Palatino']})

    # backend
    rc("text", usetex=usetex)
    rc("font", family="serif")

    # font sizes
    rc("font", size=small)  # controls default text sizes
    rc("axes", titlesize=big)  # fontsize of the axes title
    rc("axes", labelsize=medium)  # fontsize of the x and y labels
    rc("xtick", labelsize=small)  # fontsize of the tick labels
    rc("ytick", labelsize=small)  # fontsize of the tick labels
    rc("legend", fontsize=small)  # legend fontsize
    rc("figure", titlesize=big)  # fontsize of the figure title
