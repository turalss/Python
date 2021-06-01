# 1.Create a function func() which prints a text ‘Hello World’

def func():
    return('Hello World')


print(func())

# 2.Create a function which func1(name)  which takes a value name and prints the output “Hi My name is Google’


def func1(name):
    return('Hi. My name is ' + name)


print(func1('Google'))

# 3.Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when z is false it should return y . func3(‘hello’goodbye’,false)


def func3(x, y, z):
    if z:
        return x
    else:
        return y


print(func3('hello', 'goodbye', False))

# 4. Define a function func4(x,y) which returns the product of both the values.


def func4(x, y):
    return(x, y)


print(func4('a', 1))

# 5.define a function called as is_even that takes one argument , which returns true when even values is passed and false if it is not.


def is_even(num):
    if num % 2 == 0:
        return(True)
    else:
        return(False)


print(is_even(2))

# 6. Define a function that takes two arguments, and returns true if the first value is greater than the second value and returns false if it is less than or equal to the second.


def compare(num1, num2):
    if num1 > num2:
        return(True)
    else:
        return(False)


print(compare(2, 3))

# 7. Define a function which takes arbitrary number of arguments and returns the sum of the arguments.


def arbitrary_args(*arg):
    summ = 0
    for i in arg:
        summ += i
    return(summ)


print(arbitrary_args(1, 2, 3))

# 8. Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even.


def check_even(*args):
    new_list = []
    for i in args:
        if i % 2 == 0:
            new_list.append(i)
    return(new_list)


print(check_even(1, 2, 3))

# 9. Define a function that takes a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase


def upper_lower(string):
    result = ''
    for i in string:
        if string.index(i) % 2 == 0:
            result += i.upper()
        else:
            result += i.lower()

    print(result)


print(upper_lower('Tural'))


# 11.Write a function which takes  two-strings and returns true if both the strings start with the same letter.

def compare_strings_first_char(string1, string2):
    char1 = string1[0].lower()
    char2 = string2[0].lower()
    print(char1, char2)
    if char1 == char2:
        return(True)


print(compare_strings_first_char('hi', 'Ho'))

# 12. A function that capitalizes first and fourth character of a word in a string.


def capitalize_char(string):
    updated_string = ''
    for i in string:
        if string.index(i) == 0 or string.index(i) == 3:
            updated_string += i.upper()
        else:
            updated_string += i

    return(updated_string)


print(capitalize_char('tural'))
