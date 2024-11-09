# Python 3 Tuples - Introduction

#   We can consider tuples as being immutable lists, meaning their contents cannot be changed by adding, removing or replacing elements

# Tuples may prove to be useful when you want to store data in the form of sequence and keep the data untouchable

# However, unlike sets, tuples are ordered collections of non-unique elements, meaning indexes and duplicates are allowed.

# Lets start to practise and create our first tuple

# Tuples are enclosed by parentheses and their elements seperated by commas.

my_tuple = ()

# check type
print(type(my_tuple)) #returns <class 'tuple'>

# If you want to create a tuple with a single element you have to use a trick, meaning that, although you have only one element inside the tuple, you have to write a comma after it, otherwise it will not be regarded as a tuple.
# Lets see this in a practical

my_tuple = (9)
print(type(my_tuple)) #returns <class 'int'>

my_tuple = (9,)
print(type(my_tuple)) #returns <class 'tuple'>

# Now, you have a tuple set up. You should always remember this when creating tuples having only one element

# Next, lets populate our tuple with more elements

my_tuple = (1, 2, 3, 4, 5)

# Just like strings and lists, tuples support indexing, if you want to access an element within the tuple, the indexing rules we have seen are still applicable

#  Access the first element
print(my_tuple[0]) #Returns 1

# Access the last element
print(my_tuple[-1]) #returns 5
print(my_tuple[4]) # returns 5

# Since tuples are immutable, you cannot modify an element of a tuple.
# lets check this
# my_tuple[1] = 10 Type error: 'tuple' object does not support item assignment

# Also, removing elements is not permitted when working with tuples.
# del my_tuple[0] # TypeError:'tuple'object does not support item deletion

# Another interesting thing you can do with tuples is tuple assignment, This means you can assign a tuple of variable to a tuple of values and map each variable in the firsttuple to the corresponding value in the second tuple.

# lets see this as well,. Lets define tuple1 with the following elements
tuple1 = ("Cisco", "2600", "12.4")

# And now, lets assign a tuple of variables to tuple1
(vendor, model, ios) = tuple1

# Finally, lets check if the assignment and variable-to-value mapping has been properly performed.
print(vendor)
print(model)
print(ios)

# This is also called tuple packing and unpackng and you can see it as a kind of mapping between elements of two different tuples.

# An important thing to remember is that both the tuples should have the same number of elements. Otherwise , if ou have different number of elements, a ValueError will be returned.

# tuple2 = (1, 2, 3, 4)
# (x, y, z) = tuple2 # ValueError: too many values to unpack (expected 3)

# You see that tuple2 has 4 elements, but the tuple we're tryong to map it with has only 3 elements. This will generate this error message above

# You can also assign value in a tuple to variable in another tuple within a single statement, which is even more convinient
(a, b, c) = (10, 20, 30)
print(a)
print(b)
print(c)

# Next lets see some operations and methods for working with tuples


# Pytho 3 Tuples - Methods

# As with strings and lists, we can perform some basic operations on tuples , too

# We can use the len() function to find out the number of elements of  a tuple
tuple2 = (1, 2, 3, 4)

print(len(tuple2))

# Also, we have the min() and max() functions available for finding the lowest and greatest value inside a tuple
print(min(tuple2)) #returns 1
print(max(tuple2)) #returns 4

# we can also concatenete and multiply a tuple, using the same old plus and multiplication oprators

# Tuple concatenetion
print(tuple2 + (5, 6, 7))

# Tuple multiplication
print(tuple2 * 4)

# Since indexing applies to tuples as it does to strings and lists, so slicing is also possible with tuples

# Lets see a couple of examples, without entering into details about slicing again, since the rules are basically identical

# (1, 2)
print(tuple2[0:2])

# (1, 2)
print(tuple2[:2])

# (2, 3, 4)
print(tuple2[1:])

# (1, 2, 3, 4)
print(tuple2[:])

# using -ve index
# (1, 2)
print(tuple2[-4:-2])

# (3, 4)
print(tuple2[-2:])

# (4, 3, 2, 1)
print(tuple2[::-1])

# (1, 3)
print(tuple2[::2])


# Another thing you cando with tuples is you can check if an element is a member of a tuple or not using 'in' and 'not in' .Lets see this
print(3 in tuple2)# returns True

print(3 not in tuple2)# returns False

print(5 in tuple2)# returns False

#  Last thing on tuples -> We can use the del command to delete the entire tuple
#del tuple2
#print(tuple2) #NameError: name 'tuple2' is not defined

#Next -> Python 3 Ranges - Introduction
