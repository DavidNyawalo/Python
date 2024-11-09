import math

#A scientific calculator 

isRunning = True

#Display the menu to the user for them to enter their choice

while isRunning:

    #create calculator menu
    print("Choose an operation from the menu\n\n1.Addition\n2.Sutaction\n3.Multiplication\n4.Division\n5Modulus\n6.Power of a number\n7.Square Root of number\n8.Logarithm\n9.Sine\n10.Cosine\n11.Tangent\n")
    
    #ask the user for their choice
    operation = input("Enter your choice:")
    
    # 1. Addition
    if operation == "1":
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        print(f"The sum  of {num1} and {num2} is {num1+num2}")
        
        #ask the user to go back to the main menu
        back = input("Go back to the main menu? (yes/no):")
        
        if back == "yes":
            continue
        else:
            break
        
    #Subraction
    elif operation == "2":
         num1 = float(input("Enter the first number:"))
         num2 = float(input("Enter the second number:"))
         print(f"The subraction of {num1} - {num2} is {num1-num2}")
        
        #ask the user to go back to the main menu
         back = input("Go back to the main menu? (yes/no):")
        
         if back == "yes":
            continue
         else:
            break
        
        
    #Multiplication
    elif operation == "3":
         num1 = float(input("Enter the first number:"))
         num2 = float(input("Enter the second number:"))
         print(f"The multiplication of {num1} X {num2} is {num1*num2}")
        
        #ask the user to go back to the main menu
         back = input("Go back to the main menu? (yes/no):")
        
         if back == "yes":
            continue
         else:
            break
        
    
    #Division 
    elif operation == "4":
         num1 = float(input("Enter the first number:"))
         num2 = float(input("Enter the second number:"))
         print(f"The division of {num1} and {num2} is {num1/num2}")
        
        #ask the user to go back to the main menu
         back = input("Go back to the main menu? (yes/no):")
        
         if back == "yes":
            continue
         else:
            break
        
    
    #Modulus
    elif operation == "5":
         num1 = float(input("Enter the first number:"))
         num2 = float(input("Enter the second number:"))
         print(f"The modulus of {num1} and {num2} is {num1 % num2}")
        
        #ask the user to go back to the main menu
         back = input("Go back to the main menu? (yes/no):")
        
         if back == "yes":
            continue
         else:
            break
        
    
    #Power of a number
    elif operation == "6":
         base = float(input("Enter the base number:"))
         power = float(input("Enter the power:"))
         print(f"The power of {base} to {power} is {pow(base,power)}")
        
        #ask the user to go back to the main menu
         back = input("Go back to the main menu? (yes/no):")
        
         if back == "yes":
            continue
         else:
            break
        
    #Square Root of a number
    elif operation == "7":
         num1 = float(input("Enter the number:"))
         print(f"The square root of {num1}  is {math.sqrt(num1)}")
        
        #ask the user to go back to the main menu
         back = input("Go back to the main menu? (yes/no):")
        
         if back == "yes":
            continue
         else:
            break
        
    #Logarithm
    elif operation == "8":
         num1 = float(input("Enter the number you wish to find the log to base 2:"))
         print(f"The logarithm of {num1} is {math.log(num1,2)}")
        
        #ask the user to go back to the main menu
         back = input("Go back to the main menu? (yes/no):")
        
         if back == "yes":
            continue
         else:
            break
        
    #Sine
    elif operation == "9":
         num1 = float(input("Enter the angle in degrees you wish to find its sine:"))
         print(f"The sine of {num1}\u0000 is {math.sin(math.sin(math.radians(num1)))}")
        
        #ask the user to go back to the main menu
         back = input("Go back to the main menu? (yes/no):")
        
         if back == "yes":
            continue
         else:
            break
        
        
    #Cosine
    elif operation == "10":
         num1 = float(input("Enter the angle in degrees you wish to find its cosine:"))
         print(f"The cosine of {num1}\u0000 is {math.cos(math.cos(math.radians(num1)))}")
        
        #ask the user to go back to the main menu
         back = input("Go back to the main menu? (yes/no):")
        
         if back == "yes":
            continue
         else:
            break
        
        
    #Tangent
    elif operation == "11":
         num1 = float(input("Enter the angle in degrees you wish to find its tangent:"))
         print(f"The tan of {num1}\u0000  is {math.tan(math.tan(math.radians(num1)))}")
        
        #ask the user to go back to the main menu
         back = input("Go back to the main menu? (yes/no):")
        
         if back == "yes":
            continue
         else:
            break
        