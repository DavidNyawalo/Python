# Python 3 Loops - For / For-Else

# 'For' Loop

# The For statement is used whenever you want to iterate over a sequence and execute a piece of code for all or some elements of that sequence - list or string, or whatever sequence you have.

# Lets start with an example of iterating or loopnig over a sequence and, first, lets define a list.

vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

# Now, lets see how we can work with a for loop

# First, you will notice that there are some similarities to the if/elif/else syntax, meaning that the colon is again used to signal that an indented code follows for the statement. speaking about indentation, we MUST indent the code inside a for-loop

# Syntax
# We start by typing in the 'for' keyword, then we enter the iterating variable, which is a user-defined temporary variable, so you can name it however you like, then we type in the 'in' keyword, to tell Python tht we  are going to iterate/loop over the sequence following this keyword and, finally, we enter the sequence itself, followed by a colon

for each_vendor in vendors:
    print(each_vendor)

# We can also iterate over a string
my_string = "Cisco"

for letter in my_string:
    print(letter)


# Now its time to see how to use a for-loop to iterate over a range.Remember the range data type that can be used to generate an iterator over which we can iterate and then extract some values

# Lets consider a range starting at 0 and going upto, but not including 10, with a default step of 1. That would return the integers  0 all the way upto 0 , in ascending order

# Lets create this Range
my_range = range(10)

# Now lets use a for loop to iterate over this range
for i in my_range:
    print(i)


# Now, lets see a more common use aof the range() function inside a for statement. What if we want to iterate over a list using list indexes?  What do i mean by that? We still hae the vendors list in memory.
print(vendors)

# Now, remember the len() function from earlier? , lets apply it to our list
print(len(vendors))

# Now, we know that range(5) returns the integers starting with 0 upto but not including5, right?  Moreover, we can convert this range to a list , using the  list() function. Lets do thois
print(list(range(5)))# [0, 1, 2, 3, 4]

# We can look at the elements of the list as being the indexes of each elemnt of our list, vendors. So elemnt "Cisco" would be positioned at index 0 . "HP" at index 1 and so on

# This means that if we want to get a list of indexes to iterate over, using the for-loop, we can use range(len(vendors)) to obtain that list
print(range(len(vendors)))

# For now, lets crreate a for loop that prints out each elelment of the vendors lists by its index


for element_index in range(len(vendors)):
    print(vendors[element_index])


# Another very useful way to iterate over a sequence is by using both the index and the element value as iterating variables. This can be achieved by using the enumerate() function in python

for index, element in enumerate(vendors, start=1):
    # print(index, element)
    # print(f"{index + 1}. {element}")

    print(f"{index}. {element}")
    


# Python 3 Loops - While /While-Else
# The second type of Python Loops is while.
# But what is the difference between for and while loops

# Well, unlike a 'for' loop, which executes a code block a number of times, depending on the sequence it iterates over, A 'while' loop executes a piece of code as long as a user-defined codition is evaluated as True.

# If the specified condition does not change, meaning it doesn't become False, then the while-loop will continue running forever and we end up with an infinite loop

# Now, lets see an example of a while loop

# First, we should create a varaible x, with the value 1
x = 1


#  syntax
# while  condition:
    # code to execute if condition is True
    
    
    
# To create a while-loop, you have to type in the 'while' keyword, followed by the condition you want to evaluate and then a colon. Below you will specify the code to be executed as long as the condition is evaluated as True

while x <= 10:
    print(x) 
    x = x + 1 # you can also write this a x += 1
   

# .Write a Python



# The shop offers the following items with respecive prices:
# Milk - ksh 67.50
# Bread - ksh 95.00
# Eggs - ksh 20.50
# Sugar - ksh 250.00
# Tea Masala - ksh 76.99

# The program should perform the following tasks:
# 1. Prompt the shopkeeper to input the quantity of each item sold( in integers)
# 2. Calculate the total price of all items
# 3. Apply a discount of 10% if the total is over ksh1000
# 4. Display the total price and the  final balance payable by the customer

# prompt the shop keeper to enter the quantity of items bought
# variables for items
milk = 67.50
bread = 95.00
eggs =20.50
sugar = 250.00
tea_masala = 76.99





milk_quantity = int(input("enter the quantity of milk"))
bread_quantity = int(input("enter the quantity of bread"))
eggs_quantity = int(input("enter the quantity of eggs"))
sugar_quantity = int(input("enter the quantity of sugar"))
tea_masala_quantity = int(input("enter the quantity of tea masala"))



# calculate the total price
total_price = (milk * milk_quantity)+(bread * bread_quantity)+(eggs * eggs_quantity)+(sugar * sugar_quantity)+(tea_masala * tea_masala_quantity)
# Apply a discount of 10% if the total is over ksh1000
discount =  (total_price * 0.1) if (total_price > 1000) else 0.0 
#  Display the total price and the  final balance payable by the customer
final_balance = total_price - discount




print(f"The Total Price is: ksh. {total_price}")
print(f"Discount applied is: ksh. {discount}")
print(f"Final Balance is: ksh. {final_balance}")












