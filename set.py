# Python 3 sets - Introduction

#what is a set, you may ask yourself? Well, a set is basically an unordered collection of unqiue elements. Generally speking, you may regard  sets as being lists that have no duplicate elements.

# Let,s see the way to create a set. In fact, there are two ways.
# The first one is by using a set() function, which is a python built - in function.
# To also prove that sets do not allow duplicates lets crate a list  wiyh duplicate elements and apply the set() function on the list.

list4 = [1, 2, 3, 4, 5, 2, 3]
print(list4, type (list4))

print(set(list4)) # converts the list to a set(unique elements)

#So, you see the set() function removed the duolicate elements in list4, which is a very useful feature to have at hand.

#You can also directly  create a set by passing a raw sequence to the set() function, like a string or list, and referencing the result using a variable.
set1 = set([11, 12, 13, 14, 15, 15, 11])

print(set1) # return {11, 12, 13, 14, 15}

print(type(set1)) # return <class 'set'>

# the second way to create a set is to use curly braces. This method of creating a set available a set is available in versions of Python starting with 2.7, so ours is included as well, according to python.org.

set2 = {11, 12, 13, 14, 15, 15, 11}
print(set2) # return{11, 12, 13, 14, 15}

print(type(set2))# returns <class 'set'>

# we can also find out the number of elements in a set, using the same(len) function, as we did wiyh sreings and lists.
print(len(set2)) # returns 5

# Next, checking whwther an element is or is not a member of a set is also possible using the in and not in keywords:
print(11 in set2)#returns True
print(10 in set2) # returns False
print(10 not in set2) # returns True

# Going further, we have to remember that seys are mutable, so we can add or remove elements from a set, in the following manner:

#Adding
set2.add (16)# add 16 at the beginning of the set
print(set2)

#Removing
set2.remove(11)
print(set2)

# Notice if we try to add an element which already exixts in a set python will not accept, although no error is returned. It just doesnt as it.

set2.add(16) 
set2.add(16) 
set2.add(16) 

print(set2)

# python 3 sets - Methods

# To better understand set methods and operations, let's create 2 sets first.

set1 = {1, 2, 3, 4}
set2 = {3, 5, 8}

#Python defines some methods for identifying the similarities or differences between 2 sets of elements, but also other methods to better make use of this data type.

#lets see them in action.

#First, let,s see how we can identify the common elements of the two sets we defined.
#to do this, we can use the intersection() method, like this:

print(set1.intersection(set2)) # common element (s) in both sets

# And this is correct,  of course because 3 is the only element which resides in both sets. this operation can be done the other way around, too.
print(set2.intersection(set1)) # common element (s) in both sets

# Now, let's see which elements does set1 have and set2 doesnt, by using the differnce() method. Looking at the two sets, we notice that set1 has  the elements 1, 2, and 4, but set 2 does not so this should be the result, right?

print(set1.difference(set2)) #returns{1, 2, 4}

print(set2.difference(set1)) # returns{8, 5}

# To unify the two sets, you can use the union() method and the result, also being a set, a collection of unique elements, will include element 3 just once.   

#So dot confuse the union of two sets with concatenation.
print(set1.union(set2)) # returns {5, 2, 3, 8, 4, 1}

# Another thing you can do is to remove a random element in the set using the pop() method. 
set1.pop()  #removes a random element from the set-> 1
print(set1) #returns {2, 3, 4}

print(set1.pop()) # returns the removed element

#Finally, we can clear a set using the clear() method.
set1.clear() #clears the set

print(set1) #returns set

#https://docs.python.org/3/library/stdtypes.html#set

#Next -> Python 3 Tuples - Introduction

