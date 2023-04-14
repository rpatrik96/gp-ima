import numpy as np
import matplotlib.pyplot as plt
from scipy.special import digamma


def C_ima_digamma(d, D):
    return d * digamma(D / 2) - sum(
        [digamma(D / 2 + (1 - i) / 2) for i in range(1, d + 1)]
    )
