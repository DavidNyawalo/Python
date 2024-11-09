# Python 3 Booleans - Logical Operators
# As s short definition, we can say that boolean data type defines only two values -> 'TRUE or FALSE' (can only be one of them but not both)
# You can think of these values as being equivalent to 1 and 0

# In Python , true is written with a capital T and false with a capital F

# Basically, they are used to evaluate whether the expression is true or false and can be  further used in conditional or loop structures as we will see later

#  Lets see basic expessions and see how python evaluates each of them.
print(1 == 1)
# returns True

print(1 == 2)
# returns False

print("python" == "Python")
# returns False

print(3 <= 4 )
# returns True

# Ok. You got the idea. These were some pretty basic evaluations we have done

# Now, there are three main boolean operations, each of them having a specific operator namely 'and' , 'or' , 'not'

# 1 -> "and" Means both the operands should be true, in order to have the entire expression evaluated as true.

print(( 1==1 ) and ( 2==2)) 
# returns true
# Both expressions being evaluated as true, the final result is true  

print(( 1==1) and (2==3))
# returns false

# The conclusion here is that, when using the 'AND' operator, if both expessions are true, then the result will be also TRUE. On the other hand, if at least one expession is evaluated as false, then the result will be 'FALSE', as well.

# 2 -> "OR" Works like this -> if at least one of the expressions evaluates to true, then the final resultis 'TRUE' .If they are both false, then the final result will be 'FALSE', as well
# So, when using OR, it is enough if only one expression is true, in order to have 'TRUE' as the final result.

print((1 == 1) or (2 == 2))
# returns true
print((1 == 1) or (2 != 3))
# returns true
print(((1 == 1) or (2 != 3)) and ("jave" == "java"))
# returns false

# 3 -> Finally, using NOT operator means simply denying an expression. If that experssion is True, then denying it wiil result to False, and vice-versa
# Lets verify
print(not(1 == 1))
# returns false
print(not(1 == 2))
# returns true

# One more thing to keep in mind here: some Python values always evaluate to false. They are
# None
# 0
# 0.0
# empty string ""
# empty list []
# empty set set()
# empty tuple ()
# empty dictionary{}

# Python provides the bool() function to help us evaluate values and expressions as True or Flase. So, lets use this function to check the always false values

print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))


# All other values in Python are considered to be True.
print(bool(0.1))
print(bool(" "))


# Booleans and logical operators are very useful in Python, especially when dealing with 'if / else' conditionals and while loops. But more on that later

# real world example -> Login system implementation

# user credentials in the database
user_name_in_db = "Davies"
password_in_db = "P@$$w0rd"

# user credentials provided during Login attempt
user_name = input("Please enter your name : ")
password = input("Enter your password : ")

# check if the user credentials are correct
if (user_name == user_name_in_db) and (password == password_in_db):
    print("Login Successfully!!!")
else:
    print("Wrong username or Password, please try again")
    
    
# Next -> Python 3  Lists.py 
    