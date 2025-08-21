import random


Words = ("книга", "портрет", "обои")
Word = random.choice(Words)

guessed_letters = set()

attempts = 6

print("Добро пожаловать в игру 'Виселица'")

while attempts > 0:
    display_word = "".join(
        [letter if letter in guessed_letters else "_" for letter in Word])
    print("\nСлово: ", display_word)

    if "_" not in display_word:
        print("Поздравляю! Вы угадали слово: ", Word)
        break

    guess = input("Введите букву: "). lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Введите одну букву!")
        continue

    if guess in guessed_letters:
        print("Вы уже назвали эту букву!")
        continue

    guessed_letters.add(guess)

    if guess in Word:
        print("Верно!")

    else:
        attempts -= 1
        print(f"Неверно! Осталось попыток: {attempts}")


if attempts == 0:
    print("Вы проиграли! Слово было", Word)
