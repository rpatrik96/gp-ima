import numpy as np
from scipy.special import digamma


def C_ima_digamma(d, D):
    return d * digamma(D / 2) - sum(
        [digamma(D / 2 + (1 - i) / 2) for i in range(1, d + 1)]
    )


def C_ima_sample(gplvm):
    z = np.random.normal(gplvm.X.mean, gplvm.X.variance**0.5)
    dmu_dX, dv_dX = gplvm.predict_jacobian(z)  # this seems to be latents * data dim
    dv_dX[dv_dX <= 0] = 1e-6
    jacobian_sample = np.random.normal(dmu_dX, dv_dX**0.5)
    jacobian_sample = np.einsum("aik,ajk->aij", jacobian_sample, jacobian_sample).mean(
        axis=0
    )
    return np.log(np.linalg.det(np.diag(np.diag(jacobian_sample)))) - np.log(
        np.linalg.det(jacobian_sample)
    )
