# Python 3 - Lists

# a list is actually a sequence consisting of elements separated by comma. the sequence of elements is enclosed by square brackets.

# you can have any data types as an element of a list - strings, numbers, tuples, or even other lists. And a list may have any number number of ellements.

# similarly to strings, which can also be regarded as a sequence of characters, lists are indexed. meaning each element has a certain position inside the list starting at index 0.

# you can also use the len function to see the number of elements in the list and slices extract only a portion of the list. as opposed to strings, list are mutable, meaning you can modify a list by adding or removing elements.

# lets create our first list and we will name it list 1 and will be initially empty.

list1 = []

print(list1)

# to check that this is indeed a lists, lets use the old type() function on list 1

print(type(list1))  # <class 'list1'>

# now, lets add some elements to our list

list1 = ['Cisco', 'Juniper', 'Avaya', 10, 10.5, -10]

# now lets remember the len() function from string section and use it on our list
print(len(list1)) #returns 6 as the number of elements in the list

# now lets see how we can access elements in a list. the same way we deal with characters in a string, using indexes.

# Cisco
print(list1[0])
# Juniper
print(list1[1])
# -11
print(list1[5])
# 10.5
print(list1[4])

# as with strings, if we enter an invalid index, we will get an index error stating that the list index is out of range. 
# print(list1[100]) #returns index error

# to check that lists are indeed mutable, lets try to replace an element in the list.
print(list1[2])

print(list1)

list1[2] = "HP"
print(list1)


# Python 3 List - Methods

# now its time to see how to handle list and list elements and what tools does python provide for this. 

# we have already seen the len() function being used on a list but what if you want to find out the maximum or minimum value within a list, you have the max() and min() functions available for that

# lets consider list2
list2 = [-11, 2, 12]
print(min(list2))
print(max(list2))

# what about a list of strings? eg
list3 = ['a', 'b', 'c',]
print(min(list3))
print(max(list3))

print("Dennis" > "Denis")

# print(max(['a', 'b', 1, 2]))  #returns error. you cannot compare list and integers

# let's check the available list methods we have at hand.

# first we should learn how to append a new element to a list. it is simple enough coz we have the same list1
print(list1)

# to append an element to the list, judt use the append() method like this
list1.append(100)

print(list1)

# lets see how we can remove an element from a liust. you can use the following command
del list1[4] #where 4 is the index of the item we want to remove

print(list1) #removes 10.5

# another way to remove an element by its index is by using the pop method
list1.pop(0)

print(list1)

# the third way is to use the remove method.
list1.remove("HP")
print(list1)

# lets see how we can insert an element in a perticular index in the list. this is easily accomplished by using insert()
list1.insert(2, "Nortel") #2 is the index where we want the new element inserted and "Nortel" is the element we want to insert
print(list1)

# another thing we can do with lists is inserting a list to another list 

list2 = [9, 99, 999]

# to add elements of list 2 to list 1, we use extend () method
# lets see both lists first
print(list1)
print(list2)

list1.extend(list2)

print(list1) # returns ['Juniper', 10, 'Nortel', -10, 100, 9, 99, 999]

# remember index() and count() functions of strings?
# python makes them available for lists as well. lets find out

print(list1.index(-10))

# lets append another 10 to list 1
list1.append(10)

list1.count(10)
print(list1.count(10))

# first we can use the sort method
print(list2)

list2.append(1)
list2.append(25)
list2.append(500)

print(list2)

list2.sort()  #sorts in ascending order.
print(list2)

# lets see how to sort in descending order. we have the reverse() method for this. lets apply the reverse() method and check the results

list2.reverse()
print(list2)

# the two methods youve seen are modifying the list in place. after youve applied the method, theres no new list created. lets see a new method using the sorted() function. lets see it in action now:

# lets sort elements of list 2 in ascending order

# sorted(list2, reverse = False)

sorted_list = (sorted(list2))
print(sorted_list)
print(list2)

# what if we want the same function to reverse the order with a new argument inside the parenthesis.the argument is passed to the function right

print(sorted(sorted_list, reverse = True))
print(list1 + list2) #adds both lists together

print(list2 * 3) # repeats list 2 3 times

# Python 3 Lists: Slices

# the general syntax for slicing is:
# The name of the variable pointing to the list, followed by square bracket, next, in between brackets, we have a collon, on the left side of the colon we specify the index at which to start the slicing. the slice will go up to but not including the index specified.

list3 = [1, 2, 3, "a", "b", "c"]

print(list3)

# positive indexes
print(list3[0:3])
# [1, 2, 3]
print(list3[2:5])
# [3, 'a', 'b']
print(list3[2:6])
# [3, 'a', 'b', 'c']
print(list3)
# [1, 2, 3, 'a', 'b', 'c']

# negative indexes
print(list3[-4:-1])
# [3, 'a', 'b']
print(list3[-3:])
# ['a', 'b', 'c]
print(list3[:-3])
# [1, 2, 3]

# a step
print(list3[::2])
# [1, 3, 'b']
print(list3[::-1])
# ['c', 'b', 'a', 3, 2, 1]