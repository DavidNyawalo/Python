# Python 3 Numbers - Math Operators

# Python defines three numerical types namely:
# -> integers
# -> floating-point numbers
# -> complex numbers

# The complex numbers are usually used in some advanced math operations and are not of great interest for our current needs. Instead we will work alot with integers and floating-point numbers and thats why we will focus on these two numerical types and their corresponding operators and functions.

# Let's define a variable and assign it an integer and another variable associated with a floating point number, or float.
# By the way, a float type refers to real numbers, having a decimal point positioned in between the integer part and fractional part.

# Consider the following variables
num1 = 10
num2 = 2.5

print(type(num1)) #<class 'int'>
print(type(num2)) #<class 'float'>

# check the type of these variables -> type() function

# lets see what operators are able to perform using intergers and floating numbers 

# Arithmetic Operations
x = 20
y = 6
# Addition-> '+'
print(f"The sum is:{x+y}")

# Subtraction -> '-'
print(f"The difference is:{x-y}")

# Multiply -> '*' 
print(f"The product is:{x*y}")

# Division -> '/'
print(f"The quotient is:{x/y}")

# Integer division -> '//' (return the integer after the division) 
print(f"The integer after division is:{x//y}")

# Modulo -> '%' (means finding the remainder after division of 2 numbers)
print(f"The modulus is:{x%y}")

# Raising to power -> '**'
print(f"The power of {x} raised to {y} is:{x**y}")

print("====" *30)
# Comparison operators

a = 20
b = 6

# greater than -> '>'
print(f"Is {a} > {b} ? {a > b}")
# less than -> '<'
print(f"Is {a} < {b} ? {a < b}")
# less than or equal to -> '<='
print(f"Is {a} <= {b} ? {a <= b}")
# grater than or equal to -> '>='
print(f"Is {a} >= {b} ? {a >= b}")
# equal to -> '=='
print(f"Is {a} == {b} ? {a == b}")
# not equal to -> '!=' 
print(f"Is {a} != {b} ? {a != b}")

# what if we have to deal with multiple operators within the same expression. which operator have priority over others?
# well, the order is the following:
# firstly, the raising to the power option has the highest priority. it will always be eveluated first
# then, multiplication, division and modulo, with equal priorities. 
# and lastly, addition and subtraction with equal priorities

# lets see an example"
print(100 - 5 ** 2 / 5 * 2)
100 - 25 / 5 * 2
100 - 5 * 2
100 - 10
90

# lets look at 2 types of conversions.
# lets see how we can convert an integer to a float and vice versa. the good thing is that python has 2 functions available for this operation. lets see them

print(int(1.7))
# this result is 1 because int will round down to in parethesis to the nearest integer, which is 1, in this case

# next we have 
print(float(2))
# the result is 2.0. the float function will add this .0 converting 2 from an integer to a floating number.

# more functions
# 1. the abs()nfunction returns the absolute value. this is actually the number we provide and 0.

print(abs(5)) #returns 5
print(abs(-5)) #returns 5

# lets compare 2 numbers
# the max() returns the largest number
print(max(1,2)) #returns 2

# the min() returns the smallest number
print(min(1,2)) #returns 1

# lets see another way of raising to a power

# pow(x, y) where x is the base number, y is the exponent
print(pow(3, 2)) #returns 9


# write a python program that asks the user for the radius of a circle and then outputs the circumference and area of a circle
p = 22/7
r = float((input('provide the radius')))
d = r * 2
a = p * r **2
print(f"The perimeter of a circle whose radius is radius is {r} and circumference of {p * d}cm has an area of {a}cm\u00b2")

# write a python program that prompts the user to for their name and age, and outputs the user info including their name, decades lived, and second they have lived in a nice pormat.

name = input("provide name")
a = int(input("input age"))
decade = int(a/10)
second = (a *31536000)

print(f"My name is {name} and I am {a} years old. I have lived for {decade} decades which is equivalent to {second} seconds")

db_name = input("Enter username")
db_password = input("Enter password")

name = ("David")
password = ("daudi1")

if (db_name == name) and (db_password == password): 
    print("Login successfull!")
else:
    print("Wrong username and password!!!")