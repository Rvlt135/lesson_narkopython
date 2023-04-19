#task 1
school = {
    "1А": 30,
    "1Б": 28,
    "1В": 26,
    "2А": 31,
    "2Б": 27,
    "3А": 25,
    "3Б": 24,
    "3В": 25,
    "3Г": 29
}
#task 2
print(school["3В"])
#task 4
school["1А"] = 31
school["2А"] = 30
school["3А"] = 27
school["4А"] = 25
school["4Б"] = 23
del school["3Г"]
print(school)
