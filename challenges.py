# Write a programm that gets the name, age and scores for five subjects of a student. The program should store the student information in a list then compute the average score for the student. output the student score card in a nice format.


# get the user name
student_name = input("please enter your name:")
# get the user age
student_age = int(input("enter your age:"))

# create a variable to hold the student grade
grade = ""


# get the user scores for the five subjects
math = int(input("enter math score:"))
english = int(input("enter english score:"))
biology = int(input("enter bilology score:"))
geography = int(input("enter geography score:"))
kiswahili = int(input("enter kiswahili score:"))
# create an empty list to store the scores
# ##subjects = [student_name,student_age,math,english,biology,geography,kiswahili]
subjects = []
# add all the scores to our list
subjects.append(student_name)
subjects.append(student_age)
subjects.append(math)
subjects.append(english)
subjects.append(biology)
subjects.append(geography)
subjects.append(kiswahili)
# calculate the total score
total_score = subjects[2] + subjects[3] + subjects[4] + subjects[5] + subjects[6]
total_score = sum(subjects[2:])
print(total_score)
# calculate the average score
average_score= total_score/5
print(average_score)



# calculate the grade
if average_score >= 80 and average_score <= 100:
    grade = "A"
    
elif average_score >= 70 and average_score <= 79:
    grade ="B"
elif average_score >= 60 and average_score <= 69:
    grade ="C"
elif average_score >= 50 and average_score <= 59:
    grade = "D"
elif average_score >= 0 and average_score <= 49:
    print("E")
else:
    print("invalid grade")
# output the student score card
print(f"Hello{student_name}, you are {student_age} years old. And scored {average_score}% out of {len(subjects[2:])} subjects which is Grade: {grade}.")



# after the programe has calculated the average score for the student, display the grade based on the following grading table

# Range     Grade
# 80 - 100  A
# 70 - 79   B
# 60 - 69   C
# 50 - 59   D
# 0 -  49   F