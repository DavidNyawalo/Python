# Python 3 Conditionals - If / Elif / Else

# In Python we have the if, elif and else statements for decision making

# Using these statements, Python evaluates expressions and runs a piece of code accordingly, meaning if an expression is evaluated as True, then the code indented below the if statement will be executed. Otherwise, Python goes further and evaluates the 'elif' or 'else' statements if any

# Unlike many other programming languages that use  curly braces or other delimeters, Python uses indentation to define code blocks, meaning, if , for and while blocks, functions and classes

# Using indentation means that whitespaces are used as delimeters for code blocks

# Another thing to remember is that after everyif / for / while statement of function or class definition, you must use a colon, so that Python will know that it should expect anindented block right after that statement

# Now, lets start working with if, elif and else statements 

# Lets say we define a variables x = 10. And we want to make a decision, based on that value.
# Maybe the value x will change at some point during execution of the program and we want to handle that change in some particular way and run a piece of code

# Lets use the if statement to execute a block of code, if the expression we provide will be evaluaed as True
x = 10

if x > 5:
    print("x is greater than 5")

if x > 5:
    print("x is greater than 5")
    print(x * 2)

x = 4 
if x > 5:
    print("x is greater than 5")
    print(x * 2)


# Now, lets see how to use else and return to our variable x which is equal to 4
# Lets print "x is greater than 5" if indeed greater than 5, and, "x is NOT greater than 5" in any other case. This can be accomplished in the following way

x = 4

if x > 5:
    print("x is greater than 5")
else:
    print("x is NOT graeter than 5")


# The else statement is used to cover all other cases not covered by the if statement above it. So, if the expression following the 'if' keyword is True, the indented code below it will be executed. Otherwise , if the expression is evaluated as False, the indented code below else gets executed

# But, what if we want to be more granular and specify more cases and possible outputs in our program? Then we coul use the elif statement

# Lets say we want to print "x is greater than 5" if x is indeed greater than 5, "x is equal to 5", incase  x is equal to 5 at some point and " x is less than 5" for all other cases. We should then add the elif statement in between if else.

# The else statement should always be the last in an if/elif/else block

x = 4

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")



