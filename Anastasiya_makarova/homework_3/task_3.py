import random

def computer_number():
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))

def bulls_and_cows(secret_number, guess):
    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1

    return bulls, cows

def play_game():
    secret_number = computer_number()
    attempts = 0

    while True:
        user_number = input("Введите четырехзначное число с неповторяющимися цифрами: ")

        if len(user_number) != 4 or not user_number.isdigit():
            print("Некорректные данные")
            continue

        attempts += 1
        bulls, cows = bulls_and_cows(secret_number, user_number)

        print(f"Быков: {bulls}, Коров: {cows}")

        if bulls == 4:
            print("Вы выиграли!")
            break

        if attempts == 10:
            print("Вы проиграли.")
            break

play_game()
