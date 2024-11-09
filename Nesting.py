# python 3 - Nesting - If / For / While

# You can use nesting with control flow statements like if, for and while, to enable a certain behavior and logic inside your Python program. Think of nesting as using an if statement inside another if statement, a for loop inside another for loop or a while loop within another while loop. Let's use some basic examples, to see what I mean.
# First, let's refer to if statements and code blocks.
# When nesting an if statement inside another if statement, we are actually telling Python that the inde

x = "Cisco"
if "i" in x:
    if len(x) > 3:
        print(x, len(x))

if "i" in x and len(x) > 3:
    print(x, len(x))

# now lets have a look at the nested for loop

# Let's assume we have two lists and we want to multiply each element of the first list by each element of the second list. 

# For this, we should iterate/loop over both lists at the same time, take each element into account, do the multiplications and return the results. 

# Let me write this file and we will discuss it afterwards.

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for x in list1:
    for y in list2:
        print(x*y) #4x10, 4x20, 4x30, 5x10, 5x20, 5x30, 6x10,6x20,6x30
    print(x)

# so nesting a for loop inside another for loop can be prety useful
# now lets take a look at while loops

x = 1
while x <= 10:
    print(x)
    x += 1

# now lets write a nested while structure and then we will analyze it
x = 1

while x <= 10:
    z = 5
    x += 1
    while z <= 10:
        print(z)  #5 6 7 8 9 10
        z += 1

# Now, let me save the file and execute it using the Windows cmd. The result is 5 6 7 8 9 10 printed out 10 times. 

# The first while loop does the same thing as it did before. It checks whether x is less than or equal to 10 and, as long as this is expression is True, it increments x by one unit; the new thing here is the nested while loop, which gets executed each time the first while loop is executed.

# Now, if we look carefully at the second while loop, we notice that it basically does the same thing as the outer loop, meaning it takes the value of z, which is initially 5, compares it to 10, then increments it by 1 unit; it does this as long as z is less than or equal to 10. This means - as long as z is equal to 5, 6 ,7, 8, 9 or 10.

# So, the final result consists of the result of the nested while loop, which is 5 6 7 8 9 10, printed out 10 times, due to the first while loop, which performs

# write a program that gets a number from a user an prints the times table for that number from 1 to 12

# list3 = [5]
# list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for x in list3:
    # for y in list4:
        # print(x*y)

# i = 1
# j = int(input("enter number"))

# while i <= 12:
    # print(j, "x", i, "=", j*i)
    # i += 1

    # x = int(input("enter number"))

    # for y in range(1, 13):
        # print(f"{x} x {y}={x*y}")


for x in range(1,13):
    for y in range(1, 13):
        print(f"{x} x {y} = {x*y}")
    print("==="*10)

