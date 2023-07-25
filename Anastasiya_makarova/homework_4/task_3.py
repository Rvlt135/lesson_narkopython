# task 1
def positive_numbers_generator(numbers):
    for num in numbers:
        if num > 0:
            yield num

# task 2
def word_len_generator(sentence):
    words = sentence.split()
    for word in words:
        if word.lower() != "the":
            yield len(word)

# task 3
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result

