sentence = " thequick brown fox jumps over the lazy dog"
words = sentence.split()
print([len(i) for i in words if i != "the"])