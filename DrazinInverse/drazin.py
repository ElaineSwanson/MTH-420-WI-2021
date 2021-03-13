# drazin.py
"""Volume 1: The Drazin Inverse.
<Name> Elaine Swanson
<Class> MTH 420
<Date> 3/4/2021
"""

import numpy as np
from scipy import linalg as la


# Helper function for problems 1 and 2.
def index(A, tol=1e-5):
    """Compute the index of the matrix A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
        k (int): The index of A."""

    # test for non-singularity
    if not np.isclose(la.det(A), 0):
        return 0

    n = len(A)
    k = 1
    Ak = A.copy()
    while k <= n:
        r1 = np.linalg.matrix_rank(Ak)
        r2 = np.linalg.matrix_rank(np.dot(A,Ak))
        if r1 == r2:
            return k
        Ak = np.dot(A,Ak)
        k += 1

    return k


# Problem 1
A = np.array([[1,3,0,0],[0,1,3,0],[0,0,1,3],[0,0,0,0]])
Ad = np.array([[1,-3,9,81],[0,1,-3,-18],[0,0,1,3],[0,0,0,0]])
ka=1
B = np.array([[1,1,3],[5,2,6],[-2,-1,-3]])
Bd = np.array([[0,0,0],[0,0,0],[0,0,0]])
kb=3
def is_drazin(A, Ad, k):
    """Verify that a matrix Ad is the Drazin inverse of A.
    Parameters:
        A ((n,n) ndarray): An nxn matrix.
        Ad ((n,n) ndarray): A candidate for the Drazin inverse of A.
        k (int): The index of A.
    Returns:
        (bool) True of Ad is the Drazin inverse of A, False otherwise."""
    if (np.allclose(np.dot(A,Ad), np.dot(Ad,A)) 
        and np.allclose(np.dot(np.linalg.matrix_power(A,k+1), Ad), np.linalg.matrix_power(A, k)) 
        and np.allclose(np.dot(np.dot(Ad,A),Ad), Ad)):
   #np.allclose(): checks if two arrays are element-wise equal within a tolerance.
        return True
    else:
        return False
print(is_drazin(A, Ad, ka))
print(is_drazin(B, Bd, kb))
                
# Problem 2
A = np.array([[0,0,2],[-3,2,6],[0,0,1]])

def drazin_inverse(A, tol=1e-4):
    """Compute the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
       ((n,n) ndarray) The Drazin inverse of A.
    """
    n, n = np.shape(A)
    T1, Q1, k1 = la.schur(A, sort = lambda x: abs(x) > tol) #Sort the Schur decomposition with 0 eigenvalues last.
    T2, Q2, k2 = la.schur(A, sort = lambda x: abs(x) <= tol) #Sort the Schur decomposition with 0 eigenvalues first.
    
    U = np.column_stack((Q1[:, :k1], Q2[:, :n-k1])) 
    U_inv = np.linalg.inv(U)
    V = np.dot(np.dot(U_inv, A),U)
    
    Z = np.zeros((n, n))
    V1 = V[:k1,:k1]

    if k1 != 0:
        M_inv = np.linalg.inv(V1)
        Z[:k1,:k1] = M_inv
    return np.dot(np.dot(U, Z), U_inv) #UZU^(-1)
print(drazin_inverse(A, tol=1e-4))

# Problem 3
A = np.array([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]])
def effective_resistance(A):
    """Compute the effective resistance for each node in a graph.

    Parameters:
        A ((n,n) ndarray): The adjacency matrix of an undirected graph.

    Returns:
        ((n,n) ndarray) The matrix where the ijth entry is the effective
        resistance from node i to node j."""
    n = np.shape(A)[0]
    D = np.diag(np.sum(A, axis=1))
    L = np.subtract(D, A) #Laplacian
    I = np.eye(n)
    R = np.zeros_like(A, dtype=np.float64) #must be float
    for j in range(n):
        Lt = L.copy() #replace ith row
        Lt[:,j] = I[:,j]       
        Ld = drazin_inverse(Lt)
        R[:,j] = np.diagonal(Ld) #replace ith column of R with diagonal of Drazin inverse.
        R[j,j] = 0
    return R
print(effective_resistance(A))