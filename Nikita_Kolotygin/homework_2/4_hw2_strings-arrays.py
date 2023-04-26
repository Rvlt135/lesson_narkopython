
a_str = "Robin Singh"
a_list = a_str.split()
print('a_list =', a_list)

b_str = "I love arrays they are my favorite"
b_list = b_str.split()
print('b_list =', b_list)

c_list = ["Ivan", "Ivanou"]
c_str = "Minsk"
d_str = "Belarus"
print("Привет, ",c_list[0],c_list[1],"! Добро пожаловать в", c_str,d_str)

e_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(e_list))

g_list = [1,2,3,4,5,6,7,8,9,10]
g_list[2] = 33
del g_list[5]
print(g_list)