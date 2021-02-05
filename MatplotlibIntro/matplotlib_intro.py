# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Name> Elaine Swanson
<Class> MTH 420
<Date> 1/29/2021"""

import numpy as np
from matplotlib import pyplot as plt

# Problem 1
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

print(var_of_means(3))

print('\n')   

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

print('\n')
 
# Problem 2
def prob2():
    """Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution."""
    x = np.linspace(-2*np.pi, 2*np.pi, 3000)
    plt.plot(x, np.sin(x), x, np.cos(x), x, np.arctan(x))
    return plt.show()

print(prob2())

print('\n')

# Problem 3
def prob3():
    """Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6]."""
    x1 = np.linspace(-2, 1, 200, endpoint = False)
    x2 = np.linspace(1, 6, 200)
    x2 = x2[1:]
    y1 = 1/(x1-1)  
    y2 = 1/(x2-1)  
    plt.plot(x1, y1, 'm--', linewidth=4)
    plt.plot(x2, y2, 'm--', linewidth=4)
    plt.xlim(-2, 6)
    plt.ylim(-6, 6)
    return plt.show()

print(prob3())

print('\n')

# Problem 4
def prob4():
    """Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi].
        1. Arrange the plots in a square grid of four subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line."""
    
    x = np.linspace(0, 2*np.pi, 3000)
    y = np.sin(x)
    z = np.sin(2*x)
    
    ax1 = plt.subplot(221)
    ax1.plot(x, y, 'g-')
    ax1.set_title("ax1")
    ax1.set(xlim=(0, 2*np.pi), ylim=(-2, 2))
    
    ax2 = plt.subplot(222)
    ax2.plot(x, z, 'r--')
    ax2.set_title("ax2")
    ax2.set(xlim=(0, 2*np.pi), ylim=(-2, 2))
    
    ax3 = plt.subplot(223)
    ax3.plot(x, 2*y, 'b--')
    ax3.set_title("ax3")
    ax3.set(xlim=(0, 2*np.pi), ylim=(-2, 2))
    
    ax4 = plt.subplot(224)
    ax4.plot(x, 2*z, 'm:')
    ax4.set_title("ax4")
    ax4.set(xlim=(0, 2*np.pi), ylim=(-2, 2))
    
    plt.suptitle('All Subplots')
    return plt.show()

print(prob4())
    
print('\n')

# Problem 6
def prob6():
    """Plot the function f(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of f, and one with a contour
            map of f. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Add a colorbar to each subplot."""
    x = np.linspace(-2*np.pi, 2*np.pi, 1000)
    y = np.linspace(-2*np.pi, 2*np.pi, 1000)
    X, Y = np.meshgrid(x, y)
    g = (np.sin(X)*np.sin(Y))/(X*Y)

    plt.subplot(121)
    plt.pcolormesh(X, Y, g, cmap ='cool', shading='auto')
    plt.colorbar()
    plt.xlim(-2*np.pi, 2*np.pi)
    plt.ylim(-2*np.pi, 2*np.pi)
    
    plt.subplot(122)
    plt.contour(X, Y, g, 7, cmap ='ocean')
    plt.colorbar()
    plt.xlim(-2*np.pi, 2*np.pi)
    plt.ylim(-2*np.pi, 2*np.pi)
   
    plt.suptitle('Heat map and Contour')
    return plt.show()

print(prob6())

print('\n')
    
if __name__ == "__main__":
    print("Lab 4 complete.")