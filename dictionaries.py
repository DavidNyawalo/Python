# Python3 Dictionaries - Introduction

# Okay, lets study another important data type taht you will need for your python and analytics adventure -> Dictionaries

# A dictionary is an unordered set of 'key-value' pairs, seperated by comma and enclosed by curly braces

# They are very useful for storing information in a specific format. For instance, considering a router
# "Vendor": "Cisco", "Model": 2600, "IOS": 12.4, "Ports": 4

# Dictionaries are mutable, which means we cann modify their contents using dictionary-specific procedures, Why do I say dictionary-specific?  Because, unlike strings or lists , dictionaries are not indexed by the position of each element

# Dictionaries are indexed by the key. the key is the value on the left side of the colon of each key value pair. we wiil practise don't wory

# For now lets jutst create an empty dictionary

dict1 = {}

print(dict1)

# check the type
print(type(dict1))
      
#   this is how you create an empty dictionary, now, lets add some data to it

dict1 = {"Vendor": "Cisco", "Model": 2600, "IOS": 12.4, "Ports": 4}

print(dict1)

# Each dictionary element consists of a key, a colon and a value, followed by a comma.

# Now, lets notice a few things here:

# First, because the keys in our dictionary are actually strings, each key is enclosed by quotes. This  may be the most widely spread data type used for a dictionary. You may also use a number as a key, in order to have some kind of numbering system, list this

d1 = {1: "first element", 2: "Second element"}

# Ok, lets get back to our dict1 dictionary

# A key thing to remember here is that each key in the dictionary must be unique and should be of  an immutable type ->This means you can have strings, numbers or tuples as keys but not lists.

# On the other hand, values don't have to be unique and can be eitheer of a mutable or immutable data type.


# Python 3 Dictionaries - Methods

# Lets consider dict1

# First, lets extract the corresponding value for a specified key. This can be done similarly to accessing elements inside a list, only that we don't specify an inde, we specify the associated key for the value we want to extract

print(dict1)

# extract 12.4
print(dict1["IOS"])

# Remember, we said dictionaries are mutable, So, lets try to add a new key-value pair to our dictionary. This is done by simply assigning a new value to the new key.
# Add a new key-value pair to dict1 "RAM": "128"
dict1["RAM"] = "128"
print(dict1)

# Now, maybe we want to modify the value of 'IOS' data of  this device.
# Don't worry, its preety simple -  just use the same yntax as we did for adding a new pair

# Change IOS value to 15.6
dict1["IOS"] = 15.6

print(dict1)


# We can also delete a pair from the dictionary, using the del command
del dict1["Ports"]

print(dict1)

# Next, remember the len() function from strings, lists and tuples? We can use it here, as well, to find out the number of key-values pairs inside a dictionary.

print(len(dict1))

# You can verify if a certain string is a key in a dictionary or not, like this

print("IOS" in dict1) #returns True
print("IOS2" in dict1) #returns False
print("IOS2" not in dict1) #returns True

# There are three important methods to deal with keys and values in a dictionary

# The first is keys() method. This method is used to obtain a list having the keys in a dictionary as elements

print(dict1.keys())

print(list(dict1.keys()))


# The second is values() method. This method is used to obtain a list having the values in a dictionary as elements

print(dict1.values())

print(list(dict1.values()))

# The third is called items() method. This method returns a  list of tuples, each tuple containing the key and value of each dictionary pair

print(dict1.items())

print(list(dict1.items()))

# create a list of persons dictionaries with a name ,age and a list of hobbies for each person. Fill any data you want

person =[ {"Name": "Davies", 
           "Age": 23,
           "Hobbies": ["Hiking","Reading","Photography"]
           },
          {"Name": "Bob",
           "Age": 21, 
           "Hobbies": ["Cooking","Playing","Traveling"]
           },
          {"Name": "Ethan",
           "Age": 22, 
           "Hobbies":[ "Cycling","Gardening","Drawing"]
           }
]
print(person)

# extract "Traveling"
print(person[1]["Hobbies"][2])

# create a dictionary with keys a, b, c having a list of integers 1-10, 11-20, 21-30 as its values
dict = {
    "a":list(range(1,11)),
    "b":list(range(11,21)),
    "c":list(range(21,31))
    }

print(dict)

# extract 13
print(dict["b"][2])
     




 
