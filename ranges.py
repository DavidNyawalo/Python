# Python3 Ranges - Introduction


# In this lecture we will have a brief look over the range datatype and, to make things even more interesting, we will start with a quick comparison with the meaning of 'range' in the previous major version of Python2

# For this, we will open up codeskulptor.org, which is in online Python2 interpreter and we will use the range() function, by passing the value 10 as an argument

# In Python2, what range() does is it generatesa list of integers, stsrting at 0 and going up to , but not including, the value 10

# As you can see, the range() function has a default starting point at 0 and a default step of 1, since we get these consecutive integers returned
# print(range(10))

# But, don't worry, these can be customized as well.
# For example , lets start our list at 5, instead of 0.
# To do this we just have to enter a new argument, also called 'start', in between parentheses

# print(range(5, 10))

# Next, lets assume that we don't want numbers being generated - instead we want to also have a step of 2. All you have to do is to enter the step you need as the  third argument inside the parentheses
# [0, 2, 4, 6, 8]
# print(range(0, 10, 2))

# [-2, -4, -6, -8]
# print(range(-2, -10, -2))

# [-10, -8, -6, -4, -2, 0, 2]
# print(range(-10, 4, 2))

# Python 3 Range - Methods

# Ok, following up on the previous lecture, let's get into the python 3 interpreter andsee how does range () behave in Python version3 .

# Let's consider a basic implementation of range
r = range(10)
print(r)
print(type(r))

# You can easily notice taht unlie python  version2, where we would have got a list returned, in python3 , range gets its own data type <class range>

# However, if you want a list instead of a range object, you can simply apply the list() finction to this range

print(list(r))