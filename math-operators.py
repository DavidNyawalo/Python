# Python 3 Numbers - Math Operators

# Python defines three numerical types namely:
# -> integers
# -> floating-point numbers
# -> complex numbers

# The complex numbers are usually used in some advanced math operations and are not of great interest for our current needs. Instead we will work alot with integers and floating-point numbers and thats why we will focus on these two numerical types and their corresponding operators and functions

# Let's define a variable and assign it an integer and other variable associated with a floating point number, or float
# By the way, the float type refers to real numbers having a decimal point positiond in between the integer part and fractional part

# Consider the following variables
num1 = 10
num2 = 2.5
# check the type of these variables -> type() function

print(type(num1))
# returns <class 'int'>
print(type(num2))
# returns <class 'float'>


# lets see what operations we are able to perform using integers and floating-point numbers

x = 20
y = 6


#  1. Addition -> '+'
print(x+y)

#  2. Subtraction -> '-'
print(x-y)

#  3. Multipliction -> '*'
print(x*y)

#  4. Division -> '/'
print(x/y)

#  5. Integer division -> '//' (returns the integer from a division)
print(x//y)

#  6. Modulo -> '%' ( this means finding out the reminder after the divison of one number by another)
print(x%y)

#  7. Raising to a power -> '**'
print(x**y)

# write a python programm that asks the user for the radius of a circle and the returns the perimeter and the area of the circle
# define PI 
PI = 22/7
print(PI)

# prompt the user for the radius
radius = float(input("Please enter the circle radius:"))

# compute the circumference of the circle
perimeter = PI * (radius + radius)

# compute the area of a circle
area = PI * (radius * radius)
area = PI * (radius **2)
# output the results in a nice format
 
print(f"the perimeter and area of a circle whose radius is {radius}cm, is {perimeter}cm and {area}\u00b2 respectively.")



#   2. Comparison operators (returns (True OR False))
a = 20
b = 6
# less than -> '<'
print(a < b)
# returns False

# greater than -> '>'
print(a > b)
# returns True

# less than or equal to -> '<='
print(a <= b)
# returns False

# greater than or equal to -> '>='
print(a >= b)
# returns True

# equal to -> '=='
print(a ==b )
# returns False

#  not equal to -> '!='
print(a != b)
# returns True  
 
# ORDER OF OPERATIONS IN PYTHON

#  Lets talk about the order of evaluation for this operators inside a mathematical expression.
# what if we have to deal with multiple operators within the same expression? Which operations have priority over others?

# Well, the order is as follows:
# 1 -> firstly, the rasing to a power has the highest priority -> this means it will be evaluated first.
# 2 -> Then, we have the multiplication, division and modulo operations with equal priorities
# 3 -> We have addition and subtration, also with equal priorities.

# lets see an example
print(100 - 5 ** 2 / 5 * 2)

# Conversions
# lets look at two types of conversions

# lets see how we can convert  an integer to a float and vice-versa
# Well, Python has two  functions available for these operations. lets see them

print(int(1.7)) 
# the result is '1' because the int() function will round down the number in between the parentheses to the nearest integer. which is 1

print(float(2))
#  the result is 2.0 , the float() function will add .0, converting 2 from integer to a floating-point number.

# Finally, lets have a look at a few function which may come in handy in the future when working with numbers.

#  1 -> abs() : returns the absolute value. this is actually the distance between the number we provide and zero.
print(abs(5))
# returns 5
print(abs(-15))
# returns 15 

#  2 -> max() : returns the largest number between  two numbers
print(max(2, 10 ))
# returns 10

#  3 -> min() : returns the smallest number between two numbers
print(min(2, 10))
# returns 2

#  4 -> pow() : another way of raising to a power using built-in Python function
# pow(a, b ) where 'a' is the base number and 'b' is the xponent
print(pow(10, 3))
# returns 100

# write a Python program that prompts the user to enter their name and age .The program will then output the decades and seconds  the user has lived print out the results in a nice format

# Get user name
user_name= input("enter your name:")
# Get user age
user_age= int(input("enter your age"))
# Convert age lived to seconds
age_in_seconds=365*0.25*24*60*60
# Convert user age into decades lived
decades_lived= user_age//10

print(f"Hello, {user_name}, you are {user_age} years old, you have lived for {decades_lived} decade(s) and {age_in_seconds} seconds.")







# Next -> Python 3  Booleans - Logical Operators