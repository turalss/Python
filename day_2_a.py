# Write a string that returns just the letter ‘r’ from ‘Hello World’
# For example, ‘Hello World’[0] returns ‘H’.You should write one line of code. Don’t assign a variable name to the string.

hello_world = 'Hello World'
print(hello_world[8])

# 2.	String slicing to grab the word ‘ink’ from the word  ‘thinker’
# S=’hello’,what is the output of h[1]

s = 'hello'
print(s[1])  # output is 'e'

thinker = 'thinker'
print(thinker[2:5])

# 3. S=’Sammy’ what is the output of s[2:]”

sammy = 'Sammy'
print(sammy[2:])  # outpur is 'mmy'.

# 4. With a single set function can you turn the word ‘Mississippi’ to distinct character word.


def split_string(string):
    return [char for char in string]


mississippi = 'Mississippi!'
print(split_string(mississippi))

# 5. The word or whole phrase which has the same sequence of letters in both directions is called a palindrome.


def palidrome(data):
    result = []
    data = data[1:]
    for string in data:
        if ''.join(e for e in string if e.isalnum()).lower() == ''.join(e for e in string if e.isalnum())[::-1].lower():
            result.append('Y')
        else:
            result.append('N')
    return(result)


data = [3, 'Amore, Roma', 'No "x" in Nixon', 'Was it a cat I saw?']
print(palidrome(data))
