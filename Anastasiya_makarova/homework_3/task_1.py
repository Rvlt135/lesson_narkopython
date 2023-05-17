def count_likes(*names):
    if names:
        if any(ord(character) >= 0x0400 and ord(character) <= 0x04FF for character in names[0]):
            lang = 'russian'
        elif any(ord(character) >= 0x0041 and ord(character) <= 0x005A or ord(character) >= 0x0061 and ord(character) <= 0x007A for character in names[0]):
            lang = 'english'
        else:
            lang = 'unknown'

        if lang == 'russian':
            if len(names) == 1:
                return f"{names[0]} нравится это"
            elif len(names) == 2:
                return f"{names[0]} и {names[1]} нравятся это"
            elif len(names) > 2:
                return f"{names[0]}, {names[1]} и еще {len(names) - 2} человек(а) нравятся это"
        elif lang == 'english':
            if len(names) == 1:
                return f"{names[0]} likes this"
            elif len(names) == 2:
                return f"{names[0]} and {names[1]} like this"
            elif len(names) > 2:
                return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
            else:
                return "no one likes this"
        else:
            return "Некорректное значение"
    else:
        return "no one likes this"

names = input('Введите имена через запятую: ').split(',')
names = [name.strip() for name in names]
print(count_likes(*names))