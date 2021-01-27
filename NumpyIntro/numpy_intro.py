# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Name> Elaine Swanson
<Class> MTH 420
<Date> 1/22/2021
"""

import numpy as np
# Problem 1
def prob1():
    """Define the matrices A and B as arrays. Return the matrix product AB."""
    A = np.array([[3, -1, 4], [1, 5, -9]])
    B = np.array([[2, 6, -5, 3], [5, -8, 9, 7], [9, -3, -2, -3]])
    return np.dot(A, B)
print(prob1())

print("\n")

# Problem 2
def prob2():
    """Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A."""
    A = np.array([[3, 1, 4], [1, 5, 9], [-5, 3, 1]])
    return (-1) * np.dot(np.dot(A, A), A) + (9) * np.dot(A, A) - (15) * A
print(prob2())

print("\n")

# Problem 3
def prob3():
    """Define the matrices A and B as arrays. Calculate the matrix product ABA,
    change its data type to np.int64, and return it."""
    A = np.triu(np.ones((7, 7), dtype = np.int)
    B = 5 * np.ones((7, 7), dtype = np.int) - 6 * np.tril(np.ones((7, 7), dtype = np.int))
    ABA = np.dot(A, np.dot(B, A))
    C = ABA.astype(np.int64)
    return C

print("\n")

# Problem 4
def prob4(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])"""
    B = np.copy(A)
    mask = B < 0
    B[mask] = 0
    return B

A = np.array([-1, -3, -5, 0, 2, 1])
print(prob4(A))
    
print("\n")

# Problem 5
def prob5():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size."""
    
print("\n")

# Problem 6
def prob6(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])"""
    
print("\n")


    
