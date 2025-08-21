import random

options = ["камень", "ножницы", "бумага"]

while True:
    player = input("Выбери (камень, ножницы, бумага) или 'выход': ").lower()
    if player == "выход":
        print("Игра окончена!")
        break
    if player not in options:
        print("Неверный ввод.Попробуй снова.")
        continue

    computer = random.choice(options)
    print(f"Компьютер выбрал: {computer}")
    if player == computer:
        print("Ничья!")
    elif (player == "камень" and computer == "ножницы") or (player == "ножницы" and computer == "бумага") or (player == "бумага" and computer == "камень"):
        print("Ты выйграл!")
    else:
        print("Ты проиграл!")
