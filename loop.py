# python-for/while loops
# for loop
# the for statement is used whenever you want to iterate over a sequence and execute a piece of code for all or some elements in that sequence-list or string or whatever sequence you have.

# lets start with an example of iterating or looping over a sequence first, lets define a list

vendors=["cisco","hp","nortel","avaya","juniper"] 

# now lets see how we can wok with a for loop

# first you will notice that they are some similarities to the if/elif/else syntax, meaning that the colon is again used to signal that an indented code folows the for statement and, speaking about indentation we must indent the code inside a for loop using the tab key, in order to separate it from the code that follows.

# for loop syntax
# we start by typing in the for keyword, then we enter the iterating variable, which an user-defined temporary variable, so you can name it however you like.. then we type in the in keyword, to tellpython that we are going to iterate  over the sequence following this keyword and, finally, we enter the sequence itself, followed by a colon

for each_vendor in vendors:
  print(each_vendor)

# we can iterate over a string
  my_string="cisco"

  for letter in my_string:
    print(letter)
    print(letter*2)
    print(letter*3)
# so using a for statement, we assign each character in the string to a temporary variable called letter and each timw we do this, pyton executes the indented code block below the for statement. this means that for each letter in cisco, pythonprints out the character itself, the same character doubled and then tripled
  
# now its time to see how to use a loop to iterate over a range. remebr we discussedthe range data typeearlier in the course, that can be used to genrate an iterator over which we can iterate and then extract some values.
    
# lets consider a range starting from 0 and going upto but not nnot including 10 , with the default step of 1. that would return the integers 0 all way to 9 in ascending ordeer. lets get to python interpreter and create this range
  
my_range=range(10)

# now , lets use a loop to iterate over this range
 
for i in my_range:
  print(i)

for i in my_range:
  print(i*2)
# now lets see a common use of the range function inside a for statement. what if we want to iterate  over a list using list indexes?what do i mean by that?we still have the vendors list in memory
print(vendors)

# now remeber the len function from earlier? lets apply to a list
print(len(vendors))

# we know that range(5) returns the integers starting with 0 upto but not including 5, right however, we can convert this range to a  list using the list function

print(list(range(5)))

# we can look at the elements of this list as being the indexes of each elemnt of our list, vendors. so, the element "cisco" would be positioned at index 0, "hp"  at index 1 and so on

# this means that if we want to get a list of indexes to iterate over, using for a for loop we can use range(len(vendors)) to obtain that list i will explain tis shortly. for now to use this practice, lets create a for loop that prints out each element of the vendors  list by its index

for element_index in range(len(vendors)):
  print(vendors[element_index])

# so, what we did here is we passed the result of one function, len() to another function, range(). the result  is a range, consisting of all the indexes in the vendors list. we then assigned each index in this range to the element_index temporary variable and executed a piece of code for each index.
# in translation we told python to check the length of the vendors list, then create a range using that length as an argument for the range() function. finally python prints out each element , by its index: vendors[0] , vendors[1] and so on till  the list is exhausted
  
# another very useful way to iterate ove r a sequnce is by using both the index and the element value as iterating variables. this can be used by the enumerate() function
  
for index, element in enumerate(vendors):
  print(index,element  )

# write the python programm that takes a student name and their scores for five subjects as input. the programm should store the scores in a dictionary,where the keys are the student names, and the vallue are the list of their score. calculate the average score and then display the students grade based on the following criteria.

# average score>=90: A
# average score>=80: B
# average score>=70: c
# average score>=60 D

# get the number of students
num_students=int(input("please enter the number of students"))
# initialize an empty dictionary
student_score={}

# iterate over the number of students and get their names and scores 
for i in range(num_students):
  name=input(f"enter the name of student {i + 1}:")
  scores = [int(score) for score in input(f"enter the scores for{name}(separated by spaces):").split()]
  student_score[name]= scores

# calculate the average score and grade for each student
for name, scores in student_score.items():
  average_score=sum(scores)/len(scores)
  if average_score>=90:
    grade="A"
  elif average_score>=80:
    grade="B"
  elif average_score>=70:
    grade="C"
  elif average_score>=60:
    grade="D"
  else:
    grade="f"
  print(f"{name} average score is {average_score}% and their grade is {grade}")


