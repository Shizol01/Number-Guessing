import random

def guessing_number(number):
    '''
    This function will give you a random number between 1 and 100
    and make a loop untill the number is guessed
    :param int number:
    :rtype: string
    :return: Information if you guessed the number or if it's too low or too high
    '''
    random_number = random.randint(1, 100)
    while number != random_number:
        number = input("Guess a number: ")
        while not number.isdigit():
            print("It's not a number!")
            number = input("Guess a number: ")
        number = int(number)
        if number > random_number:
            print("Too big!")
        elif number < random_number:
            print("Too small!")
        else:
            print("You win!")

guessing_number(0)