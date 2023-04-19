import string
from collections import Counter

text = input("Введите текст: ")
counter = Counter(filter(lambda c: c.lower() in string.ascii_lowercase, text))
common_letter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))[0][0]
print(common_letter)
