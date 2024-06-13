"""
This script is part of introduction of computer science for EE students.
"""

# Empty dictionary
tel = {}
print("tel:", tel)
# Define a new dictionary
tel = {'jack': 4098, 'sape': 4139}
print("tel:", tel)
# Add (or replace) a pair
tel['guido'] = 4127
print("tel:", tel)
# What is the value of the key 'jack'?
print("tel['jack']:", tel['jack'])

# This will raise KeyError as abby is not a key in the dictionary
try:
    print("tel['abby']:", tel['abby'])
except KeyError:
    print('abby is not a key in tel dictionary')

# This will raise TypeError as keys must be immutable
try:
    a = {(1, 2, 3, [1, 2]): "wrong"}
except TypeError:
    print('keys must be immutable')

# dictionary methods
tel = {'sape': 4139, 'jack': 4098, 'guido': 4127, 'irv': 3555}

# remove a pair
print("tel.pop('sape'):", tel.pop('sape'))
print("tel:", tel)
# alternatively, use del that will not return the value
# del tel

# get the keys  - returns a list, order is arbitrary
print("tel.keys():", tel.keys())

# check if a key is in tel
print("'guido' in tel:", 'guido' in tel)

# Get value of key
print("tel.get('jack'):", tel.get('jack'))
print("tel.get('Jack', 'Missing'):", tel.get('Jack', 'Missing'))

# convert a list of pairs (tuples or lists) to a dictionary
dict_example = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print("dict_example:", dict_example)

# Update: add dict2 to dict1
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Gender': 'female'}
dict1.update(dict2)
print("dict1:", dict1)

# student grades - given a name we want to know the grade
students_grades = [("Thomas", 100), ("Arthur", 40), ("John", 56)]


# using a list
def get_grade_list(students, name):
    for stud in students:
        if stud[0] == name:
            return stud[1]


# using a dict
def get_grade_dict(students, name):
    return students.get(name)


print("get_grade_list(students_grades, \"Thomas\")", get_grade_list(students_grades, "Thomas"))
students_grades_dict = dict(students_grades)
print("get_grade_dict(students_grades_dict, \"Thomas\")", get_grade_dict(students_grades_dict, "Thomas"))

# Dictionaries can be used to store complex data sets. While keeping everything indexed and organized
phonebook_dict = {'meni': {'office': 97286421234, 'fax': 97286421234, 'mobile': 972526421234},
                  'jinji': {'office': 97286421234, 'mobile': 972526421234, 'email': "mail_address@gmail.com"}
                  }
print("phonebook_dict[\"jinji\"][\"email\"]:", phonebook_dict["jinji"]["email"])


