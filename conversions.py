# Python 3 - Conversions between Data Types

# The last thing we should cover on the Data Types topic

# This means that you will learn hiw to convert from one data type , a number for example, to another data type, like a string

# These are specific functions that accomplish these tasks, lets see some of them in action

# First, lets try to convert an integer of floating- point number to a string. This can be achieved by using the str() function

num = 2
f = 2.5

# check the type of variables
print(type(num))
print(type(f))

# now, converting a number to a string
num2 = str(num)
print(type(num2), num2)

f2 = float(f)
print(type(f2), f2)

# Now, lets try backwards and convert a string to an integer, using the int () function

str1 = "5"
print(type(str1), str1)

int1 = int(str1)
print(type(int1), int1)

# You can also convert integers to floating point numbers, using the float() function, and vice versa using the same int() function we've seen

num2 = 2

f = float(num2)
print(f)

# Now, the other way around, from float to integer using int() function
f = 2.5
int1 = int(f)
print(int1)











































# Now, moving to sequences, lets convert a tuple into a list, using the list() function

tuple1 = (1, 2, 3)
print(type(tuple1)) #<class 'tuple'>

# convert a tuple into a list
list1 = list(tuple1)
print(type(list1)) #<class 'list'>

# We have also seen how the set() funtion works for turning a list into aset
set1 = set(list1)
print(type(set1))

# The last thing I'll showw here is how to convert between different numerical representations of numbers and I am referring to decimal, binary, and hex notations,so base-10, base-2, and base -16 numbers
# for this, we will need the  bin(), hex() and int() functions.

num = 10

# convert to binary
num_bin = bin(num)
print(num_bin)

# convert to hexadecimal
num_hex = hex(num)
print(num_hex)

# Now, to convert from binary and hex format back to decimal notation, we will use the int () function

# convert binary  to decimal
bin_to_num  = int(num_bin, 2)
print(bin_to_num)

# convert hex to decimal
hex_to_num = int(num_hex, 16)
print(hex_to_num)


# Next -> Python 3 Conditionals - If/ Elif/ Else