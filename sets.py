# Python 3 sets- introduction

# What is a set, you may ask yourself?. Well it is an unordered collection of unique elements.

# Lets see the way of creating a set. In fact, there are two ways.

# The first one is by using the set() function, which is an inbuilt function.

# To also prove that sets do not allow duplicates, lets create a list with duplicate elements and apply the set() function on this list.

list4=[1,2,3,4,5,2,3]
print(type(list4), list4)

# Converting the list to a set
print(set(list4)) #{1,2,3,4,5}
# A list is closed of with square brackets while a set is enclosed with calibraces

# You see that the set() function removed the duplicate elements in list 4 which is a very useful feature to have at hand.

# You can also directly create a set by passing a raw sequence to the set() function, like a string or list and referencing the results using a variable

set1=set([11,12,13,14,15,15,15,11])
print(set1)

print(type(set1),set1)

# The second way to create a set is to use curly- braces. This method of creating a set is available in versions of python starting with 2.7 according to python.org

set2={11,12,13,14,15,15,15,11}
print(set2)
print(type(set2))

# We can also find out the number of elements in a set, using the same len() function as we did with strings and lists
print(len(set2))# reteuns 5 (sets do not allow duplictes)

# Now, checking whether an element is or is not a member of a set is alaso possible using the 'in' or 'not in' keywords

print(11 not in set2)#Returns false
print(11 in set2)#Returns true
print(16 not in set2)#returns true

# We have to remember thet sets are mutable, so we can add or remove elements from a set in the following manner

# Adding an element to a set ->add() method
set2.add(16)
print(set2)

# Removing an element from a set
set2.remove(11)
print(set2)

set2.add(16)
print(set2)

# Notice that if you try to add an element which already exists in the set, python will not agree although no error is returned. It just doesn't add it.

# Now lets see some operations and methods that can be applied to sets.

# Python 3 sets - Methods
# To better understand set methods and operations lets create two sets first
set1= {1,2,3,4}
set2= {3,5,8}

# Python defines some methods for idenifying the similarities or differences between two sets of elements, but also to better make use of this data type. Lets see them in action

# First, lets ee how we can identify the common elements of the sets we defined
# To do this, we can use the intersection() method like this
print(set1.intersection(set2))
print(set2.intersection(set1))

# Now, lets see which elements does set1 have and set2 doesn't by using the difference() method
print(set1.difference(set2))#{1,2,4}
print(set2.difference(set1))#{5,8}

# Tou unify the 2 sets we can use the union() method and the result also being a set, a collection of unique elements, will include element '3' just once. So do not confuse the union () method with concatenetion() method
print(set1.union(set2))#{1, 2, 3, 4, 5, 8}


# Another thing you can do is remove a random element in the set by using the pop() method
print(set1.pop())
print(set1)

# So we can clear a  set using the clear() method 
print(set1.clear())
print(set1)
print(type({})) # returns dictionary

# Next   Python 3 Tuples - Introduction
