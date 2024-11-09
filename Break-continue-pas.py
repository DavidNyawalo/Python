# Break
# The break and continue statements are used to handle the flow of a while or a for loop in a Python program, meaning the programmer can interrupt or restart the execution of a loop structure, in certain conditions.

# Let's start with the break statement, which is used to terminate the loop in which it resides.

# To show how break works, we will first create a new file, called break.py and write a for loop.

for number in range(1, 11):
    if number == 7:
        break
    print(number)

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for x in list1:
    for y in list2:
        if y == 20:
            break
        print(x*y)
    print("Outside the nested loop")

# Continue
# Now let's have a look at the continue statement.
# When Python stumbles upon a continue statement inside a for or while loop, it ignores the rest of the code below, for the current iteration, goes up to the top of the loop and immediately starts the next iteration.
# In order to see this in practice, let's consider the same lists and for loops as earlier, but replace break with continue in our file.


list1 = [4, 5, 6]
list2 = [10, 20, 30]

for x in list1:
    for y in list2:
        if y == 20:
            continue
        print(x*y)
    print("outside the nested loop")

# finally lets talk about pass statements
# pass is the equivalent of "do nothing". It is actually just a placeholder, for whenever you want to leave the addition of a piece of code for later and move on to write other segments of your program.

# Let's see a short example of this, in the Python interpreter.

for number in range(10):
    pass

print("continue here...")

if True:
    pass

def greet():
    pass

