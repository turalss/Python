# 1. Create a list with one number, one word and one float value. Display the output of the list.

all_type_list = [0, 'Tural', 30.5]
print(all_type_list)

# 2. I have a nested list [1,1[1,2]], how to grab the value of 2 from the list.

get_number_from_list = [1, 1, [1, 2]]
print(get_number_from_list[2][1])

# 4. Create a dictionary with weekdays an keys and week index numbers as values.do assign dictionary to a variable

week = {
    'Sunday': 7,
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
}

# 5. D={‘k1’:[1,2,3]} what is the output of d[k1][1]

d = {'k1': [1, 2, 3]}
print(d['k1'][1])  # output is 2

# 6. Can you create a list [1,[2,3]] into a tuple

my_list = [1, [2, 3]]
print(tuple(my_list))  # yes, you can

# 7. With a single set function can you turn the word ‘Mississippi’ to distinct character word.


def split_string(string):
    return [char for char in string]


mississippi = 'Mississippi!'
print(split_string(mississippi))

# 8. Can you add an element ‘X’ to the above created set

# yes, you can
string_to_char = split_string(mississippi)
string_to_char.append('X')
print(string_to_char)

# 9. Output of set([1,1,2,3])

print(set([1, 1, 2, 3]))  # unique and sorted values

# 10. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

result = []
for n in range(2000, 3200):
    if n % 5 != 0 and n % 7 == 0:
        result.append(n)
print(result)

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:


def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


print(factorial(8))
