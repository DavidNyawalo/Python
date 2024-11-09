# Python 3 - Strings

#  Lets define a strin first
#  A string is a sequence of characters, meaning -> letters, numbers and other characters like 'dollar-sign', spaces and punctuation marks enclosed by single quotes, double quotes, or even triple quotes when spanning multiple lines.

# Lets define a string and assign it to a variable 
my_string = "this is my first string"
print(my_string)
my_string = 'this is my first string'
print(my_string)

# What do we need triple quotes for? We need them whwnever we want to enter a string on multiple lines -> for inistance, a comment in our code

my_string = '''this
is
my
first
string'''
print(my_string)

# Indexing
# Python uses indexing to mark the position of an element within a sequence of elements -> a string is a sequence of elements and the elements of a string are the character themselves, one character one element.

# The first element of any any sequence, when counting from left to right, has the index 0 , the second of the sequence has index 1 and the third positioned in the has index 2

# So when using indexes, remember to count from 0

# When counting backwards, from right to left, the first index will be -1.
# The last character in a string will have the index -1, when looking from right to left.

# The indexes are enclosed by square brackets, when we want to access some letter from a string.

# Lets see this in practice

string1 = "Cisco Router"

# Now, how to extract the first character of this string? By using an index, of course. And as stated,  that would be index 0. So, to access the elements of string1, positioned on index 0 we should type the following


# The name of the variable, stirng 1 and then, without inserting any spaces, the index number in between brackets, so 

print(string1[0])  
# Returns C

# Lets find the third character of string1. What index should we use?
print(string1[2])
# Returns s

# Lets see the sixth element
print(string1[5])
# Returns white space character

# Now, for negative(-) indexes. Lets access the last character in the string -> We would index negative 1 (-1)
# Returns r (last element)

# What about
print(string1[-4]) 
# it would return u

# One more thing on indexes -> What if we enter an invalid index for our string?

# Lets see what I mean by this?
# First, lets find out strings1's length.
# We can count how many characters are in the string visually, but what if we have a very very long string, maybe a newspaper page?
# Python has a solution for this and its called the "len()" function.

# This function is easy to use, just type len and without any spaces after it, add the variable name pointing to our string in between parentheses.

print(len(string1))
# Returns the number of characters , which is 12

# Back to the first question, what happens if we enter an invalid index?
# Lets try this
# print(string1[20])
# Returns IndexError : string out of range



# Python 3 - String Methods

# We've talked about indexing and how we can determine the length of a sequence, in our case a string, using the len() function.

# Now, lets see other operations
#  1. First, one more thing about indexes -> you an find out the index of a character ini a given string by using the indexing() method.
# Just remember that this method returns the first occurrence of that particular character in the string

a = "Cisco Switch"

# You can clearly see that letter 'i' appears two times in the string. So lets find out the index of the first occurrence of 'i' in this string
print(a.index("i"))
# Returns 1

# explanation (syntax)
# We have the name of the variable associated with the string, 'a', then a dot, then the name of the method, 'index()', then, in between parentheses, we enter the character we want to find out the index for, 'i'.

# 2. Another useful Python method is one that helps you to find out how mwny times does a character appear in a string or generally speaking, an element inside a particular sequence, This method is called 'count()'

# The syntax of count() is similar to the one of the index() method.
# To use the count() method, just type the name of the variable , then a dot, then the word 'count', then open and close parentheses and finally, the letter you want to count sorrounded by quotes.
print(a.count("c")) 
# Returns 2

# 3. Another string method is find() . This method simply searches for a sequence of characters inside the string and if it finds a match, then it returns the index where the sequence begins.
print(a.find("sco")) 

#  On the other hand if Python does not find a match, then it will return the value '-1' . Let test this and search for the substring "xyz"
print(a.find("xyz"))
# returns -1

# if a.find("s") == -1:
    # print("the subsrting was not found in the string")
# else:
    # print("Found!!!")            
    
        
    

# 4. We can also use some predefined Python methods to turn a string from uppercase to lowercase or vice-versa, if we want that.
# This can be accomplished by using the lower() and upper() methods

print(a)
# lowercase
print(a.lower())

# uppercase
print(a.upper())

print(a)
#  Keep on thing in mind here! Although we have just applied the lower() and upper() methods , the initial string is still the same, no changes have been applied
#  -> this is great proof that strings are indeed immutable
print(a)




# 5.  You can also verify that a string starts or ends with a particular character or substring. We have two methods forthis namely startswth() or endswith()
print(a.startswith("C"))
#  returns True
print(a.endswith("h"))
#  returns True
print(a.endswith("i"))
#  returns False

# 6. Tree important methods which you should keep in mind, beacause you will use them a lot when working with strings, are the "strip(), split(), join()" methods

# 6.1 The strip method eliminates all white spaces from the start and the end of a string

# Lets say we have a new string , one with 3 spaces before "Cisco" and 4 spaces after "Switch"

b = "   Cisco Switch    "
# Lets apply the strip () method
print(b.strip())
# returns the cleaned string
print(b)
#  returns the initial string

# b.strip() returns "Cisso Switch" without any spaces at he beginning and at the end of the string. That's nice and may be useful, so keep that in mind.

# Now consider that instead of three spaces on  each side of the string, we had three '$' signs that we want to remove
# We want to remove the leading and trailing dollar signs. For this we should specify the character we want to remove in between the strip()'s parentheses, so:
c = "$$$Cisco Switch$$$$"
print(c)
print(c.strip("$"))

# What if we want all spaces removed from the string, ofcourse removing those inside the string? Then, we have the replace() method instead of  strip()
#  Lets refer to the string referenced by variable b, which has spaces at the end of the string

b = "   Cisco Switch    "

# You can use the replace()  method like this , to get a clean string
print(b.replace(" ", ""))

# 6.2  split() method -> As it name implies, this method simply splits the string into substring. Furthermore, you can specify a delimiter  for splitting the string. The result f this method is a list.

# Lets say we have a string referenced by a variable d like this
d = "Cisco,Juniper,HP,Avaya,Nortel"

# The network device manufacture in the string are delimited by commas. So, the comma will be regarded as our delimeter for the split.
# What if we want to extract each provider fromo the string in a nice format?
# Well, in this case, the split() methods saves the day.
# Lets type the following
print(d.split(","))
# Python returns a list where each provider in the string is an element of this list and can be further used into an application

# 6.3 join() method -> For dealing with strings
# Lets remember string 'a' -> 'Cisco Switch'
# What if we want to insert a character in between every two characters of the string? So, we want to change this string 'a' to "C_i_s_c_o__S_w_i_t_c_h"

# For this we will use the join() method the following way and it is abit dufferent than the syntax we've seen before
# First, you type in the character you wnat to use as a seperator, encolosed with double or single quotes.
# It's upto you, So this character would be the underscore character in our case.

print("_".join(a))



# Tomorrow -> Strings Operators & Formatting       
# Tomorrow -> Strings Slicing  

# What else can we do with srings??

# For instance we can concatenate them. Concatenation means unifying two or more strings into a single string
# You can di this using the '+' operator, like you would when adding two  numbers.

# Lets try,
# Lets set x with the value of 'Cisco'
x = "Cisco"
print(x)

# And y with the value "Switch"
y = "Switch"
print(y)

# And finally adding the together
space = " "
z = x + space  + y 
print(z)


# Another thing we can do is string repitition by using multiplication '*' operator
print(x * 5)

# You can also verify if a character is in a  string or not, using the "in" and "not in" operators

print("o" in x)
# returns True

print("o" not in y)
# returns True

print("S" in x)
# returns False






# Now, what's the deal with striing formatting?

# Lets say we have some kind of string template and we want to constantly modify only a few words


my_string = "Cisco model : 2600XM, 2 WAN slots, IOS 12.4"

# We want to keep this string as a template and just change the model name, number of slots and IOS version a couple of times, while running our Python program. So, this would be a dynamic change each time.

# For this we should use the perceny (%) operator, followed by letter (s) for string, (d) for digit or (f) for floating-point number. Lets see the syntax
formatted_string = "Cisco model : %s, %d WAN slots, IOS %f" %("2600Xm", 2, 12.4)
print(formatted_string)

# Now, let's translate this: the %s means that this is a placeholder for a string we will specify in between parentheses, at the end of this line.
# The %d operator follows the same logic, but for a number, instead of a string, and finally, the %f refers to afloating_point number(a number with a decimal point.)
# Now moving on, th efirst value from within the parentheses is going to  be associated with the first format operator in the string; the second value from within the parentheses is going to be associated with the second format operator in the string, and so on, for all the format operators you have in your string.
# Also, do not forget to insert the % sign between the string and the parentheses containing the values
# This operator maps the format operators inside the string with the values inside the parentheses.

("2691", 4, 12.3)
("7200", 8, 15.4)
("1841", 1, 1.2)

formatted_string2 = "Cisco model : %s, %d WAN slots, IOS %f" %("2691", 4, 12.3)
formatted_string3 = "Cisco model : %s, %d WAN slots, IOS %f" %("7200", 8, 15.4)
formatted_string4 = "Cisco model : %s, %d WAN slots, IOS %f" %("1841", 1, 1.2)
print(formatted_string2)
print(formatted_string3)
print(formatted_string4)

# Something you might have noticed is the adddition of several decimal places when dealing with floating-point numbers. In order to have this under control, you can easily choose the number of decimal places you want to print out.

# Simply insert a dot and a value between the percent operator and the letter f.
formatted_string = "Cisco model : %s, %d WAN slots, IOS %.10f" %("2600Xm", 2, 12.4)
print(formatted_string)
#  That's awsome

# However, thats not the only way of dealing with string formatting
# Instead of formatting operators like the ones we've just seen, we can use another notation, replacing %s, %d or %f with a pair of curly braces.

# Also after the string, the % operator we used for mapping the values is going to be replaced by a method called format(). lets type this
f_string = "Cisco model : {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4)
print(f_string)

# Lets say that we can use some sort of indexing when dealing with this type of string formatting.
# Lets assign a value for each of these pairs of curly braces
f_string2 = "Cisco model : {2}, {0} WAN slots, IOS {1}".format("2600XM", 2, 12.4)
print(f_string2)

# f-string formatting
first_name = "Davies"
user_age = 18
print(f"My name is {first_name}, and I am {user_age} years old") 


#   Python 3 Strings - Slices
# Slices allows us to exteract various parts of a string(or a list, or other sequence of elements).

# The syntax of a string slice is the following:

# mystring[10:15]

# We have the name of the variable pointing to the strinig, followed by a pair of squre brackets, we have a colon, on the left side of the colon, we specify the index at which to start the slicing proces. The slice will go up to, BUT WILL NOT INCLUDE, the index specified on the right side of the colon.

string1 = "O E2 10.110.8.9 [160/5] Via 10.119.254.6, 0:01:00, Ethernet2"

# Lets extract the first IP address in the string, 10.110.8.9
print(string1[5:15])

# Now, what if we don't specify the second index inside the brackets? Well, then the string slice would start at the index given before the colon and would end at the end of the string. This way we will get the rest of the string, starting from the character at index 5. lets test this as wel
print(string1[5:])

# What if we only use the second ndex, the one after the colon, but we don't specify the first index? Then, the slice will simply start at the begining of the string and would go upto, BUT NO INCLUDING, the character at the index we enter after the colon. lets try this
print(string1[:10])

# What if we don't enter any indexes at all?
print(string1[:])

# What about negative indexes?  Lets try extracting a couple of slices using negative values for our indexes
print(string1[-1])
print(string1[-2])

# What if we want to extract a slice containing the substring "Ethernet" this time using negative indexes
print(string1[-9:-1])

# What if we want to obtain the last five characters of our string? How do we do that?
print(string1[-5:])
# Leave out the last five characters
print(string1[:-5])

# One more thing about slices. You can specify a third element within the square brackets, after the indexes, also seperated by colon. This is called a step.
# For instance, if you would like to skip every second character of the string and obtain a new string with these elements removed, you can write the following slice
print(string1[::2])


# The last thing I'll show yuo is how to print out the string in reverse order, using slices and indexes. For this we will again use a slice and a step







