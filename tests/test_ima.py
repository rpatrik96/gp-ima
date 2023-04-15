from gp_ima.ima import C_ima_sample
import GPy
import numpy as np


def test_dummy():
    pass


def test_C_ima_sample():
    X = np.random.randn(10, 2)
    kernel = GPy.kern.RBF(2, ARD=False) + GPy.kern.Bias(2)
    m = GPy.models.GPLVM(np.asarray(X), 2, kernel=kernel)

    C_ima_sample(m)
