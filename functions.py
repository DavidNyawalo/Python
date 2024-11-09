#Python 3 Function ->Basics

#THis is a core topic in Python ,and ,in fact in any other programming language.

#You are going to use functions a lot to build your applications.

#But ,first,what is a function??
#Well ,you can use a function to organise your code in blocks that can be later reused .this is helpful if you want better read-ability for your code,modularity and also time saving when designing and running your code.

#Before we start coding, remember that coding follow the same syntax rules as other structures that we've seen so far.but also add some features that we're  going to analyze soon.

#First, a function is defined using "def" keyword ,followed by the name of the function ,a pair of parenthesis ,and then a colon.After the colon ,on the next row ,you will type in the code you want to store in this function.Indented one level to the right, as we did with if or for statements.
def my_first_function():
    "This is the first function"
    print("Hello , Python!")
 
#As we mentioned ,we have the "def" keyword ,the name of the function,my_first_function, then parenthesis and finally the colon .This is theh way you define a function.

#One important thing to remember is: that in between  the parenthesis youcan specify one or several parameters for the function.   

#After defing a function with or without any parameters inside the parenthesis ,we can all that function whenever we need to run inside it.

#Inorder to call a function ,you just need to type in that function's name followed by the parameters and thats it.
my_first_function()

#Now,as mentioned earlier, functions are reusable blocks of code.
my_first_function()
my_first_function()
my_first_function()
my_first_function()
my_first_function()
my_first_function()


#Another advantage of functions is that you can change the code within the function and see the results changing , as well, the next line youncall that function.So,we can say functions are dynamic structures.


#Now lets talk a bit about parameters and arguments and the difference between the two concepts.
#Lets create a new function

def greet_user(name):
    print(f"Greetings,{name}")
    
#So in this case , name is passed as a parameter as a parameter to the function and then used inside the code within function.This means that whenever we're going to call the function and pass an argumeent of our choice to tghe function ,that argument will be passed further to the code insude the function.

#Parameters are the ones written inside the parenthesis when  defing the function
#Arguments are the ones written inside the parenthesis when  defing the function

#Parameter ->a variable
#Argument -> a value to a varaible

greet_user("Davies")
greet_user("Buju")
greet_user("Morgan")
greet_user("Shabah")
greet_user("Recee")


#Multiple params
def add_two_numbers(x,y):
    sum = x + y
    print(f"The sum is: {sum}")
    
add_two_numbers ( 5,10)
add_two_numbers ( 15,10)
add_two_numbers ( 25,10)
add_two_numbers ( 6,10)

#Return statement 

#Now,we're going to talk about return statement 

#The statement is used to exit function and return something whenever the function is called.

def add (x,y):
    sum = x + y
    return sum
    
print(add (5,5))

result = add (16 , 19)
print(result)


#Create a function that takes in(parameter) list of integers and returns the smallest add integer in that list.

def smallest_integer(number_list):
    odd_numbers = []
    for i in number_list:
        if i % 2 ==1:
            odd_numbers.append(i)
    return min(odd_numbers)
    
my_list= [-3,44,50, 23]    
print(smallest_integer(my_list))

#OR
 
def smallest_integer(number_list):
    odd_numbers = []
    for i in number_list:
        if i % 2 == 1 :
            odd_numbers.append(i)
    #return min( odd_numbers)
    odd_numbers.sort()
    return odd_numbers[0]
    
my_list= [-3,44,50, 23]    
print(smallest_integer(my_list))




#create a Python progrm 5 or four function that asks the user for their name and age ,then out of the user info in a nice format display the name,age decades lived and age in seconds.

def username():
    name = input("Please enter your name:")
    return name

def user_age():
    age = int (input("Enter your age:"))
    return age

def decades_lived(age):
    user_decaded_lived = age // 10
    return user_decaded_lived

def age_in_seconds(age):
    user_age_in_seconds = age * 365.25 * 24 * 60 * 60
    return user_age_in_seconds

def display_user_info():
    name = username()
    age = user_age()
    decades = decades_lived(age)
    seconds = age_in_seconds(age)
    print(f"Hello {name}, you have lived for {decades} decades,{seconds} seconds , which means you are {age} years old.")
    
display_user_info()


