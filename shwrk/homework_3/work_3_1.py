import re

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))

def show_likes(list = None):
    # for i in list:
    #     print(i)

    # Проверка на пустой маcсив
    if list == None:
        print("Error: list = None")
        return

    # Проверка языка
    s = list[0]
    rus_lang = has_cyrillic(s)

    # Подбор значений
    n = len(list)
    if n == 0:
        print("no one likes this")
    if n == 1:
       s =  list[0]
       if rus_lang:
           print(s, "понравилось это")
       else:
           print(s, "likes this")
    if n == 2:
        s1 = list[0]
        s2 = list[1]
        print(s1, "and", s2, "like this")
    if n == 3:
        s1 = list[0]
        s2 = list[1]
        s3 = list[2]
        m = s1 + ", " + s2 + " and " + s3 + " like this"
        print(m)
    if n >= 4:
        s1 = list[0]
        s2 = list[1]
        k = n-2
        m = s1 + ", " + s2 + " and " + str(k) + " like this"
        print(m)


    # show_likes()
# show_likes([])
# show_likes(["Aaa", "Bbbb"])
# show_likes(["Aaa"])
# show_likes(["Aaa", "Bbbb", "Ccccc", "Dddddd", "Eeeeeee"])
# show_likes(["Aaa", "Bbbb", "Cccc", "Dddd"])
show_likes(["Шшавшаша"])