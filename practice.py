# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 04:08:22 2021

@author: Elaine
"""

import numpy as np
from matplotlib import pyplot as plt

def var_of_means(n):
    """Construct a random matrix A with values drawn from the standard normal
    distribution. Calculate the mean value of each row, then calculate the
    variance of these means. Return the variance.
    Parameters:
        n (int): The number of rows and columns in the matrix A.
    Returns:
        (float) The variance of the means of each row."""
    A = np.random.normal(size=(n,n))
    y = np.mean(A, axis=1)
    return np.var(y)

def prob1():
    """Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array."""

    Q = np.linspace(100, 1000, 10)
    V = [1]*len(Q)
    for j in range(len(Q)):
        V[j] = var_of_means(int(Q[j]))
    plt.plot(Q, V)
    return plt.show()

print(prob1())
