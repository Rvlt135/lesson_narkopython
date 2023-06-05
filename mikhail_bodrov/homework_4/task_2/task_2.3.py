'''Необходимо составить список чисел которые указывают на длину слов в строке: sentence = " thequick brown fox jumps
over the lazy dog", но только если слово не "the"'''

def len_words(words):
    words = words.split()
    for i in words:
        if i != 'the':
            yield len(i)

sentence = " thequick brown fox jumps over the lazy dog"

print(list(len_words(sentence)))
