a = "12345678"

print(a[0])
print(a[-1])
print(a[2])
print(a[-2])
print(len(a))

b = "somelettersin"

print(b[:7])
print(b[4:-5])
print(b[::3])
print(b[::-1])

print("My name is {name}".format(name="Mihail"))

test_tring = "Hello world!"

print(test_tring.find("w"))
print(test_tring.count("i"))
print(test_tring.startswith("Hello"))
print(test_tring.endswith("qwe"))

c = "www.my_site.com#about"

print(c.replace("#","/"))

d = input("Write something:")

print("with ing " + d + "ing")

e = "Ivanov Ivan"
e = e.split(' ')
e = e[::-1]
e = ' '.join(e)

print(e)

f = input("With space: ")
f = f.split()
f = ' '.join(f)
print(f)


