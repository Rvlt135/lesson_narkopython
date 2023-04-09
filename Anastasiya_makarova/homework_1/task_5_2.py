words = input("Cлово или слова через пробел: ")
entered_words = words.split()
words = [word + "ing" for word in entered_words]
words_with_ing = " ".join((words))
print(words_with_ing)
