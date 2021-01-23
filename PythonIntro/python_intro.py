# python_intro.py
"""Python Essentials: Introduction to Python.
<Name> Elaine Swanson
<Class> MTH 420
<Date> 1/11/2021
"""

print("\n")

# Problem 1
if __name__ == "__main__":
   print ("Bonjour, Python Coding world!")
   
print("\n")
   
# Problem 2.  
def sphere_volume(r):
    """Return the volume of a sphere with a specified radius, r."""
    return (4/3 * 3.14159 * r**3)
r=5
print(sphere_volume(r))
# Can define r before input or put number for r in the print call.
print(sphere_volume(2))

print("\n")
    
# Problem 3
def isolate(a, b, c, d, e):
    """Return positional arguments with first three separated by 5 spaces, 
    and last two with a single space between each argument."""
    print(a, b, c, sep='     ', end=' ')
    print(d, e, sep=' ', end=' ')
    # Default sep and end is one space.
    # Does not have to be just spaces. Sep and end can be any insert.
    return
(isolate(1, 0, 1, 0, 1))

print("\n")

# Problem 4
def first_half(text):
    """Returns the first half of inserted text, if string of text is
    even, returns the rounded down integer from odd string number's
    division by 2."""
    return text[0:int(len(text)/2):1]
print(first_half('Elaine'))

print("\n")

def backward(text):
    """Returns the reverse order of inserted text using slicing with
    a negative step parameter in [start:stop:step]"""
    # Negative indices count backward from the end
    # Indexing begins at 0, defaults are beginning for start
    # and end for stop
    return text[::-1]
print(backward('Swanson'))


print("\n")

# Problem 5
def list_ops():
    """Returns an alternative list of animal names than what was entered."""
    my_list = ["bear", "ant", "cat", "dog"]
    my_list.append("eagle")
    my_list[2] = "fox"
    my_list.pop(1)
    my_list.sort(reverse=True)
    my_list[1] = "hawk"
    my_list[-1] += "hunter"
    return my_list
print(list_ops())

print("\n")

# Problem 6
def pig_latin(word):
    """ Accepts a word and translates it to Pig Latin."""
    vowels = ['A', 'E', 'I', 'O', 'U', 'a','e','i','o','u']
    first = word[0]
    if first in vowels:
         word += "hay" 
         return word
    else: 
        word = word[1:]+word[0]+"ay" 
        return word 
word = "Gibson"
print(pig_latin(word))

print("\n")

# Problem 7
def palindrome():
    """Finds and returns the largest palindromic number made from the
    product of two 3-digit numbers."""
    number = 0   
    for x in range(100, 1000):
        for y in range (100, 1000):
            product = x * y 
            s = str(product)
            if s == s[::-1] and product > number:
                number = product
    return number
print(palindrome())
  
print("\n")
# Problem 8
def alt_harmonic(k):
    """Compute the sum of the alternation harmonic series of the n
    first terms."""
    return sum([((-1)**(n+1))/n for n in range(1, k+1, 1)])
print(alt_harmonic(500000))              