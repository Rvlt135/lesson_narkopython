from math import floor

#2.1 task
t_str = "Abc123ghi";
print("t_str =", t_str);

print("lenght of string is", len(t_str), "symbols");

print("test_string first symbol is", t_str[0]);
print("test_string last symbol is", t_str[-1]);
print("test_string third symbol is", t_str[2]);
print("test_string third from the end symbol is", t_str[-3]);

#2.2 task
y_str = "I am b2c test engineer";
print("y_str =", y_str);
print("First 8 symbols =", y_str[:8:]);

print("4 symbols from center of string =", y_str[floor(len(y_str) / 2) - 2:floor(len(y_str) / 2) + 2]);

print("Symbols with [3] indexes =", y_str[3::3]);
print("Reverse of string =", y_str[::-1]);

#2.3 task
my_name = "Nikita";
name_string = f"my name is {my_name}";
print(name_string);

#2.4 task
test_tring = "Hello world!";
print("Index of w-symbol is", test_tring.index("w"));
print("Count of 1-symbol is", test_tring.count("1"));

print("test_tring starts from Hello, that's", test_tring.startswith("Hello"));
print("test_tring ends with qwe, that's", test_tring.endswith("qwe"));


#2.5 task
website_url = "www.my_site.com#about";
print("Right url is", website_url.replace("#", "/"));

#2.6 task
input_text = input("Enter the word: ");
input_text = input_text+"ing";
print(input_text);

#2.7 task
ivan_string = "Ivanov Ivan";
ivan_string = ivan_string.split(" ");
print("commands is", " ".join(ivan_string));
