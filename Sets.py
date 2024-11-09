# PYTHON 3 SETS
# N/B LISTS ALLOW DUPLICATES SETS DONT

# Set is an unordered collection of unique elements. Sets are used to eliminate duplicate values, i.e  they have no duplicate.

# Sets are created by using the set() function or placing all the elements within curly braces {}.
# To also prove that sets do not allow duplicates lets create a list with duplicate elements and apply set function on this list.

list4=(1,2,3,4,5,2,3)
print(list4, type(list4))

print(set(list4)) #converts list to set of unique elements

# You can also direcly create a set by passing a row sequnce to the set() function like a string or a list and referencing the set to a variable.

set1=set([11,12,13,14,15,11,12])
print(set1) #returns {11, 12, 13, 14, 15} i.e unique elements only.
print(type(set1)) #returns <class 'set'>

# The second way of creating a set is by using the curly braces {} and passing the elements to the set. This is oly allowed to python version 2.7 and above.

set2={11,12,13,14,15,15,15,11}
print(set2) #returns {11, 12, 13, 14, 15} i.e unique elements only. 
print(type(set2)) #returns <class 'set'>

# We can also find out the number of elements in a set using the len() function.
print(len(set2)) #returns 5 i.e number of unique elements in the set.

# We can also check if an element is a member in a set using the in keyword.

print(11 in set2) #returns True
print(10 in set2) #returns False
print(10 not in set2) #returns True

# Lets check whether a set is mutable or not by trying to change an element in the set.
set2.add(16) #will add 16 at the beginning of the set. Hence sets are mutable.
print(set2)

# We can also remove an element from a set using the remove() function.
set2.remove(11) #removes 11 from the set2.
print(set2)

# Notice if we try to add an element that already exists in the set, python will not agree with us though it will not throw an error. It just won't add the element to the set.

set2.add(16)
set2.add(16)
set2.add(16) #will not add 16 to the set2 as it already exists.
print(set2) #returns {12, 13, 14, 15, 16} with only one 16.


###############################################################################
# We can also use the clear() function to remove all elements from the set.
# set2.clear()
# print(set2) #returns set() i.e an empty set.

# We can also use the del keyword to delete the set completely.
# del set2
# print(set2) #returns NameError: name 'set2' is not defined

# We can also use the union() function to combine two sets.
# set3={1,2,3}
# set4={4,5,6}
# print(set3.union(set4)) #returns {1, 2, 3, 4, 5, 6}

# We can also use the update() function to combine two sets.
# set3.update(set4)
# print(set3) #returns {1, 2, 3, 4, 5, 6}

# We can also use the intersection() function to find the common elements between two sets.
# set5={1,2,3,4}
# set6={3,4,5,6}
# print(set5.intersection(set6)) #returns {3, 4}

# We can also use the difference() function to find the elements that are in set5 but not in set6.
# print(set5.difference(set6)) #returns {1, 2}

# We can also use the symmetric_difference() function to find the elements that are in set5 but not in set6 and vice versa.
# print(set5.symmetric_difference(set6)) #returns {1, 2, 5, 6}

# We can also use the issubset() function to check if set5 is a subset of set6.
# print(set5.issubset(set6)) #returns False

# We can also use the issuperset() function to check if set5 is a superset of set6.
# print(set5.issuperset(set6)) #returns False

# We can also use the isdisjoint() function to check if set5 and set6 have no common elements.
# print(set5.isdisjoint(set6)) #returns False

# We can also use the copy() function to copy a set to another set.
# set7=set5.copy()
# print(set7) #returns {1, 2, 3, 4}

# We can also use the pop() function to remove an element from the set.
# set7.pop()
# print(set7) #returns {2, 3, 4}

# We can also use the discard() function to remove an element from the set.
# set7.discard(2)
# print(set7) #returns {3, 4}

# We can also use the difference_update() function to remove the elements that are in set5 but not in set6 from set5.
# set5.difference_update(set6)
# print(set5) #returns {1, 2}
################################################################################

# SET METHODS

set1={1,2,3,4}
set2={3,5,8}

# To check for the common elements between two sets. We use the intersection() method.
print(set1.intersection(set2)) #returns {3} i.e elements in set2 that are in set1.
print(set2.intersection(set1)) #returns elements in set2 that are in set1.

# Lets see which elements set1 has but set2 hasn't and vice versa. We use the difference() method.
print(set1.difference(set2)) #returns {1, 2, 4} i.e elements in set1 but not in set2.
print(set2.difference(set1)) #returns {8, 5} i.e elements in set2 but not in set1.

# unify two sets/concatenate two sets. We use the union() method.
print(set1.union(set2)) #returns {1, 2, 3, 4, 5, 8} i.e all elements in set1 and set2.

# We can remove a random element from the set using the pop() method.
set1.pop() #removes a random element from set1 i.e first element
print(set1) #returns {2, 3, 4} i.e set1 without the first element.
# to see removed element
print(set1.pop()) #returns 2 i.e element to be removed.

# How to clear set
set1.clear() #clears all elements in set1
print(set1) #returns set() i.e an empty set and not {} as {} is a dictionary.
# i.e
empty={}
print(type({})) #returns <class 'dict'>

# more on sets can be found at https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset


# Next -- Python 3 TUPLES
# Path: Course%20work/Class%20work/tuples.py
