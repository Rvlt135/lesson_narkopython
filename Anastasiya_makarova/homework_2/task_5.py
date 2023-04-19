first_dictionary = { 'a': 1, 'b': 2, 'c': 3}
second_dictionary = { 'c': 3, 'd': 4, 'e': 5}

joined_dictionary = {}
for key in set(first_dictionary.keys()) | set(second_dictionary.keys()):
    if key in first_dictionary and key in second_dictionary:
        joined_dictionary[key] = [first_dictionary[key], second_dictionary[key]]
    elif key in first_dictionary:
        joined_dictionary[key] = [first_dictionary[key], None]
    else:
        joined_dictionary[key] = [None, second_dictionary[key]]

print(joined_dictionary)

