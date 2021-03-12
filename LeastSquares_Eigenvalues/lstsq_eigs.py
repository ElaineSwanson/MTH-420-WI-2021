# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Name> Elaine Swanson
<Class> MTH 420
<Date> 2/10/2021
"""

import numpy as np
from scipy import linalg as la
from matplotlib import pyplot as plt

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
# from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations."""
    Q,R = la.qr(A,mode="economic")
    b2 = Q.T @ b #Or we can do... np.dot(Q.T, b)
    x = la.solve_triangular(R, b2)
    
    return x

A = np.random.random((5,2))
b = np.random.random(5)
print(least_squares(A, b))

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line."""
    x,b = np.load('housing.npy').T
    A = np.column_stack((x,np.ones((x.shape[0], 1)))) #stack col of 1s to matrix
    k, m = least_squares(A, b)
    plt.scatter(x, b)
    plt.plot([0,16],[m,10*k+m])
    return plt.show()

print(line_fit())

# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots."""
    
    x,b = np.load("housing.npy").T
    """x_dup = np.column_stack([x]*4) #stack col four times vertically
    A_m = np.column_stack((x_dup,np.ones((x_dup.shape[0], 1)))) 
    A12 = np.vander(A_m[:,0], 13)
    A9 = np.vander(A_m[:,1], 10)
    A6 = np.vander(A_m[:,2], 7)
    A3 = np.vander(A_m[:,3], 4)  
    
    x12, res12, rnk12, s12 = la.lstsq(A12,b) #Won't work with getting x alone, why?
    x9, res9, rnk9, s9 = la.lstsq(A9,b)
    x6, res6, rnk6, s6 = la.lstsq(A6,b)
    x3, res3, rnk3, s3 = la.lstsq(A3,b)
    
    #x: least-squares solution. Return shape matches shape of b.
    #residue: square of the 2-norm for each column in b - a x, if M > N and ndim(A) == n
    #s: singular values of a."""
    
    p12 = np.poly1d(np.polyfit(x,b,12)) #Polynomial with coef. from np.polyfit
    p9 = np.poly1d(np.polyfit(x,b,9))
    p6 = np.poly1d(np.polyfit(x,b,6))
    p3 = np.poly1d(np.polyfit(x,b,3))

    x_fig = np.linspace(0,16)
    y12_fig = p12(x_fig)
    y9_fig = p9(x_fig)
    y6_fig = p6(x_fig)
    y3_fig = p3(x_fig)
    
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Polynomial curve fitting')
    fig.subplots_adjust(hspace=.5)

    axs[0, 0].scatter(x, b, marker = '.', color = 'steelblue', label = 'Housing data')
    axs[0, 0].plot(x_fig, y12_fig, color = 'orangered', label = 'Fit line')
    axs[0, 0].set_title('Polynomials of degree 12')
    axs[0, 0].legend(loc = 'lower right')

    axs[0, 1].scatter(x, b, marker = '.', color = 'steelblue', label = 'Housing data')
    axs[0, 1].plot(x_fig, y9_fig, color = 'orangered', label = 'Fit line')
    axs[0, 1].set_title('Polynomials of degree 9')
    axs[0, 1].legend(loc = 'lower right')

    axs[1, 0].scatter(x, b, marker = '.', color = 'steelblue', label = 'Housing data')
    axs[1, 0].plot(x_fig, y6_fig, color = 'orangered', label = 'Fit line')
    axs[1, 0].set_title('Polynomials of degree 6')
    axs[1, 0].legend(loc = 'lower right')
    
    axs[1, 1].scatter(x, b, marker = '.', color = 'steelblue', label = 'Housing data')
    axs[1, 1].plot(x_fig, y3_fig, color = 'orangered', label = 'Fit line')
    axs[1, 1].set_title('Polynomials of degree 3')
    axs[1, 1].legend(loc = 'lower right')
    
    return plt.show()
print(polynomial_fit())
