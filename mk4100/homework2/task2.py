school = {'1a': 14, '1b': 12, '1c': 15, '2a':2, '2b': 32, '2c': 1353, '3a': 123, '3b': 53, '3c': 342, '4a': 123}

print(school.get('1a'))

school['1a'] = 15
school['2a'] = 16
school['1b'] = 54
school['4b'] = 12
school['4c'] = 11
del school['1c']

print(school)