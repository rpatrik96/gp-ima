import numpy as np
import matplotlib.pyplot as plt
from scipy.special import digamma


def C_ima(d, D):
    return d * digamma(D / 2) - sum(
        [digamma(D / 2 + (1 - i) / 2) for i in range(1, d + 1)]
    )


Ds = np.logspace(0, 3, 1000).astype(int)
plt.plot(Ds, [C_ima(max(1, int(np.log(D))), D) for D in Ds])
