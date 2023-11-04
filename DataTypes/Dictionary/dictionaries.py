#  Update / add an element to the dictionary

socials_dict = {'name': 'Edy', 'age': 26}
socials_dict['address'] = 'London'
print(socials_dict)

# methods:

socials_dict.keys()  # Returns all the keys
socials_dict.values()  # Returns all the values
socials_dict.items()  # returns a list of every itemized key:value pair

socials_dict.get('name')  # maps to a value from key input

any(socials_dict)  # logical 'or' built in
all(socials_dict)  # logical 'and' built in


#  Traverse through a dictionary

def traverse_dict(dict):
    for key in dict:
        print(key, dict[key])


traverse_dict(socials_dict)


# find keys with only the value
def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


#  Searching a dictionary


def search_dict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'


print(search_dict(socials_dict, 27))

#  Delete or remove a dictionary

socials_dict.pop('name')
socials_dict.clear()  # removes every element
socials_dict.popitem()  # removes last item in list
del socials_dict  # DELETES THE ENTIRE SHIT

# sorted method
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}

print(sorted(myDict, key=len))
