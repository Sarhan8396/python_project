oper = ['+', '-', '*', '/']


while True:
    try:
        name = input("Введите имя: ")
        print(f"Привет, {name}!")
        operator = input("Выбери оператор: ('+' ,'-' ,'*', '/')  ")
        if operator not in oper:
            print("Неверный оператор: Введите оператор! ('+' ,'-' ,'*', '/')")
            continue

        num_one = int(input("Первое число: "))
        num_two = int(input("Второе число: "))

    except ValueError:
        print("Ошибка: Должны ввести число!")
        continue

    try:

        if operator == '+':
            print(num_one + num_two)
        elif operator == '-':
            print(num_one - num_two)
        if operator == '*':
            print(num_one * num_two)
        elif operator == '/':
            print(num_one / num_two)

    except ZeroDivisionError:
        print("Ошибка: Деление на ноль нельзя!")
        continue

    answer = input("Хотите продолжить?: (да/нет) ")
    if answer == 'нет':
        break

