# What is a variable?  how to define a varaible and What is it good for, in python?

# A variable is nothing more than a reserved location in computer's memory, used to store information -values to be more precise.

# This means that when we create a variable you reserve some space in memory.

# You can store different types of adat using a variable - you can store a string, a number, a list or any other data type that you can think of.

#  Unlike other programming languages, in python you don't have to explicitly declare a variable - instead, the declaration is done automatically whe you assign a value to that variable, no matter what type of data you decide to assign to that memory location.

#e.g String username = "Dennis"; in other languages
#  username ="DAVIES"

# Frthermore, you can later access the value referenced by that variable and use it in other areas of  your Python application.

# lets think of how you should properly name a variable in Python.

# There are several rules to consider and follow for a clean and compliant code and also for avoiding any conflict with Python's built-in names.

#  First, A variable name should always start with a letter, usually lowercase and never start with a number or any symbol. However thereis one exeption to this rule- some variable names start with an underscore '_' or double underscore "__", but this are python specific structures, so lets leave them to python.

#  Second, The variable name may contain lowercase or uppercase letters, numbers and the underscore, but not as the first character

# Third, Do ont include spaces or any other special characters insid variable names -> this means no dollar signs, no commas, no parentheses, no question marks so on.


# And REMEMBER Python names are case-sensitive, so a variable named 'my_Var' is a different variable than a variable named 'my_var', with a lowercase 'v'
# Age != age !=AGE

#  Another thing about variable names is that you should keep a reasonable name length, so that it will be easier for you to remember it and reference it inside your code.

#  The last thing I should mention for this topic is that there are some PYTHON reserved names, which you cannot use a variable names.
#  e.g -> def,while,for,if,case,int,list,str

# Lets see how we can assign a value to a variable

# The rule is to use the equal sign  '=' -> this should be regarded as an assignment operator, rather than the usual equal sign used in math.

# In the left side of the equal sign you type the variable name, and in the right side you type the value you want to assign to that variable.

# It doesn't matter if you leave a space between each side of the equal sign. Actually, I would advise you to leave a space on each side of the equal sign, for better readability of your code.

# i.e num1=7
    #   num1 = 7 is recommended
    
    # You are also able to do multiple assignment, so you can assign a value to multiple variables, at the same time. The syntax for this would be
a = b = c = x = y = 10
print(a)
print(b)
print(c)
print(x)
print(y)
    
    # Also, you can assign a differnt value for each variable within the same line of code ,like this
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)