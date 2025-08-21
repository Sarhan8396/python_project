import random

print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 100. Попробуй угадать!")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Введи число: ")
    if not guess.isdigit():
        print("Пожалуйста, введи целое число!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Моё число больше!")
    elif guess > secret_number:
        print("Моё число меньше!")
    else:
        print(
            f"Поздравляю! ты угадал число {secret_number}, за {attempts} попыток")
        break
