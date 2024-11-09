import random

# Lottery Application (List/Set Comprehensions)

# Method/Functions for Implementing this app
# 1 -> getting the user lucky numbers
# 2 -> generating the winning numbers
# 3 -> Dislay menu to the user 

# a fuction to generate the winning numbers
def create_lottery_numbers():
    # create a list for the random lucky numbers
    # values = []
    # for value in range(6):
    #     values.append(random.randint(1, 50))
    # return values
    # create an empty set 
    values = set()
    # loop as long as the length of values set is less than 6
    while len(values) < 6:
        values.add(random.randint(1, 50))
    return(values)

print(create_lottery_numbers())


# a function to get user numbers for lottery draw
def get_player_numbers():
# prompt the user to enter 6 numbers
    numbers_csv = input("Enter six numbers eparated by comma(No spaces): ")
    # create a list of numbers from the number_csv

    # numbers_list = numbers_csv.split(",")
    # # create an empty set to store the number
    # numbers_set = set()
    # for number in numbers_list:
    #     numbers_set.add(int(number))
    # return numbers_set

# alternatively
    numbers_set = {int(number) for number in numbers_csv.split(",")}
    return numbers_set

print(get_player_numbers())

# a function to display the menu to the player/user
def menu():
    # ask the user for lucky numbers.
    user_lucky_num = get_player_numbers()

    # generate winning numbers
    lottery_num = create_lottery_numbers()

    # print winning numbers
    matched_num = user_lucky_num.intersection(lottery_num)

    # calculate the price
    prize = 100 ** len(matched_num)
    price = 0 if (prize == 1) else 100 ** len(matched_num)
    # print out the prize and the winning numbers
    s = "s" if (len(matched_num) > 1) or (len(matched_num) == 0) else ""
    print(f"The winning numbers are:  {lottery_num}")
    print(f"You matched {len(matched_num)} number{s} and won Ksh. {price}")

    
menu()



# print(round(random.random() * 10))

# a function to create th winning lottery numbers
