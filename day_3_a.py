import random

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). Go to the editor

result = []
for n in range(2000, 3200):
    if n % 5 == 0 and n % 7 == 0:
        result.append(n)
print(result)

# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]


def celsius_to_fahrenheit(celsius):
    return("Fahrenheit ", (9/5)*celsius + 32)


print(celsius_to_fahrenheit(36.6))


def fahrenheit_to_celsius(fahrenheit):
    return("Celsius ", (5/9)*(fahrenheit - 32))


print(fahrenheit_to_celsius(80))

# Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.


def random_number_generator():
    return(random.randint(0, 9))


def guess_number_game():
    random_number = random_number_generator()
    input_number = int(input())
    if input_number == random_number:
        return('Well guessed!')
    else:
        return guess_number_game()


# print(guess_number_game())


# 4. Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

def construct_pattern(number):
    for x in range(1, number + 1):
        print("*"*x)
    while number > 0:
        number -= 1
        print("*"*number)


print(construct_pattern(5))
