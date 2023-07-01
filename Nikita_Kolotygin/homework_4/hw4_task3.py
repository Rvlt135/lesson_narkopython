sentence = "thequick brown fox jumps over the lazy dog"

sentence_list = sentence.split(" ")
print(sentence_list)

list_len = [len(i) for i in sentence_list if i!="the"]
print(list_len)