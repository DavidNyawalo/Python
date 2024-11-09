import random

# print(round(random.random() * 10))

# a function to create th winning lottery numbers
def create_lottery_numbers():
    lottery_numbers =set()
    while len(lottery_numbers) < 6:
        
        # lottery_numbers.append(random.randint(1,50))
        lottery_numbers.add(random.randint(1,50))
 
    return lottery_numbers
   

# a function to get the user winning numbers
def user_winning_numbers():
    
    numbers = input("Enter 6 numbers separated by comma (with no spaces): ")
    # Numbers_list = numbers.spilit(",")
    numbers_list = [int(number) for number in numbers.split(",")]
    numbers_set = set(numbers_list)
    return numbers_set
    
    
# a function to display the menu
def display_app_menu():
    winning_lottery_numbers = create_lottery_numbers()
    user_lottery_numbers = user_winning_numbers()
    
    matched_numbers = user_lottery_numbers.intersection(winning_lottery_numbers)
    numbers = 0 if len(matched_numbers) == 0  else matched_numbers
    prize = 100 ** len(matched_numbers)
    print(winning_lottery_numbers)
    print(f"You matched {numbers} numbers and won ksh.{prize}")
    


# call the menu function here
display_app_menu()