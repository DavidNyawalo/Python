#Python 3 -Break,Continue and Pass

#The break and continue statements are used to handle the flow of a while or for loop in a Python program,meaning the programmer can interrupt or restart a loop structure,in certain condition.

#Lets start with the break statement ,which is used to terminate the loop in which it resided.

for number in range(10):
    if number == 7:
        break
    print(number)
    
for i in range(20):
    if i == 16:
        break
    print(i)
    

#challenge time

list1 = [4,5,6]
list2 = [10,20,30]

for i in list1:
    for j in list2:
        if j == 20:
            break
        print(i * j)
    print("Outside the nested loop")
    

#Now lets look ate the continue statement

#When Python stumbles upon a continue statement inside a for or while loop,it IGNORES the rest of the code below,for the current iteration ,goes up to the loop and immediately starts the next iteration.

list1 = [4,5,6]
list2 = [10,20,30]

for i in list1:
    for j in list2:
        if j == 20:
            continue
        print(i * j)
    print("Outside the nested loop")
    
    

#Finally , lets talk about the pass statement 

#Pass is equivalent of "do nothing".

#It is actually just a placeholder, for whenever you want tp leave the addition of a piece of code for later and move on to the other segments of your program.
#Example:
for i in range(20):
    pass

print("Hello")
