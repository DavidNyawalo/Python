# Python 3 - User Input

#  Through the course you are going to learn how to insert some  input into a Python Program.

# Actually you are going to use a specific function, in order to ask the user for some input, store the infomation he/she is entering at the prompt and the use that information further into the program.

# This is especially useful when you need to build an interractive application, usually having some sort of menu that the user needs to interact with.

# Examples of such menus are "Please enter your username:" or "Choose an option from the following list"

# The function we are talking about is called input()

# Lets propmt the user to enter a string that he/she wants to be printes out on the screen.

# Let me write the code and we analyze it inch by inch.

user_says = input("Please enter the string you wish to print: ")

# Looking at  the above liine of code, you may ask yourself what is this "user_says" thing?. Well, thats a Python variable and dont worry, we will talk more about variables very soon. For now,just keep in mind that by using a variable, you can store or save the value entered by the user, for later use.

# The so called storing or saving of the user's input is accomplished using the equal sign, which is called an assignment operator.

# Following the equal sign, we have the input() function.

# Next, inside input()'s pair of parentheses, you have to type in a description, a phrase, which is actually a string asking the user for input. This is completely upto to you with an appropriate sentence.

# A good practice here is to also enter a colon and a space after the text, so when the user inputs some data, it will be clearly seperated from the sentence you wrote -> just to make everthing pretty and easy to read.

# Finally, do not forget to enclose everything you write inbetween paretheses, also using either double or single quotes.

# Last but not least, in order to have our text printed out on the screen and visible to the user, we should use the print() function in Python, to print out the content of the user_says variable

print(user_says)


# Tomorrow -> Variables