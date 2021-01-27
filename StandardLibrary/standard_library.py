# standard_library.py
"""Python Essentials: The Standard Library.
<Name> Elaine Swanson
<Class> MTH 420
<Date> 1/21/2021"""

import calculator
from itertools import combinations

print("\n")

# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order)."""
    return min(L), max(L), sum(L)/len(L)
            
print(prob1((1, 2, 3)))

print("\n")

# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    # Integers are mutable
    
    x = int(3.0)
    y = x
    y = int(4.0)
    
    print("ints are mutable?", y == x)  
 
    # Strings are immutable
    
    string_1 = 'I love Python'
    string_2 = string_1
    string_2 += '...not'

    print("strings are mutable?", string_2 == string_1)
  
    # Lists are mutable
    
    list_1 = ["Gil", "Martijn", "Elaine", "Kim"]
    list_2 = list_1
    list_2.pop(3)
    
    print("lists are mutable?", list_2 == list_1)
    
   # Tuples are immutable
   
    tuple_1 = (0, 1, 2, 3)
    tuple_2 = tuple_1 
    tuple_2 += (1,)
    
    print("tuples are mutable?", tuple_1 == tuple_2)
    
   # Sets are mutable
   
    set_1 = {'a','b','c','d'}
    set_2 = set_1
    set_2.add('f')
    print("sets are mutable?", set_1 == set_2)      
    return

print(prob2())

print("\n")

# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than those that are imported from your
    'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    return calculator.sqrt(calculator.sigma(calculator.multiply(a, a), calculator.multiply(b, b)))
   
print(hypot(3, 4))

print("\n")

# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    my_set = []
    for i in range(0, len(A)+1):
        for combo in combinations(A, i):
            my_set.append(set(combo))
    return my_set        

A = {'a', 'b', 'c', 'd'}
print(power_set(A))

print("\n")

if __name__ == "__main__":
    print("Lab 2 complete. This was hard.")

