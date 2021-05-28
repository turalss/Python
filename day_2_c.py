# Three is a Crowd

# Make a list of names that includes at least four people.

names = ['Tural Hasanli', 'Orkhan Aliybali', 'Salchuk Asci',
         'Aynuy Carlson', 'Joseph Armstrong', 'Sevinc Hasanova']

# •	Write an if test that prints a message about the room being crowded, if there are more than three people in your list.


def check_number_of_people(room):
    if len(room) > 5:
        return('crowded')
    elif len(room) == 2 or 1:
        return('not crowded')
    else:
        return('empty')


print(check_number_of_people(names))

# •	Modify your list so that there are only two people in it. Use one of the methods for removing people from the list, don't just redefine the list.

names.remove('Tural Hasanli')
names.remove('Orkhan Aliybali')
print(names)

# •	Run your if test again. There should be no output this time, because there are less than three people in the list.

print(check_number_of_people(names))
