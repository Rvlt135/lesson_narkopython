def likes(text):
    if text:
        if any(ord(character) >= 0x0400 and ord(character) <= 0x04FF for character in text[0]):
            lang = 'russian'
        elif any(ord(character) >= 0x0041 and ord(character) <= 0x005A or ord(character) >= 0x0061 and ord(
                character) <= 0x007A for character in text[0]):
            lang = 'english'
        else:
            lang = 'unknown'

        if(lang == 'english'):
            if (len(text) == 0):
                print("no one like this")
            elif (len(text) == 1):
                print(text[0], "likes this")
            elif (len(text) == 2):
                print(text[0], "and", text[1], "likes this")
            elif (len(text) == 3):
                print(text[0], ",", text[1], "and", text[2], "likes this")
            else:
                print(text[0], ",", text[1], "and", len(text) - 2, "others likes this")
        elif (lang == 'russian'):
            if (len(text) == 0):
                print("Никому не нравится")
            elif (len(text) == 1):
                print(text[0], "нравится это")
            elif (len(text) == 2):
                print(text[0], "и", text[1], "нравится это")
            elif (len(text) == 3):
                print(text[0], ",", text[1], "и", text[2], "likes this")
            else:
                print(text[0], ",", text[1], "и", len(text) - 2, "другим нравится это")
        else:
            print("Введите русские или английские имена")
    return text

print("Введите имена через запятую:")
text=input().split(",")
likes(text)


