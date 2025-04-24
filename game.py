import random
target_number = random.randint(1, 100)
attempts = 0  # Счётчик попыток
while True:
    user_input = input("Введите ваше число: ")
    try:
        number = int(user_input)  # Преобразуем ввод в число
    except ValueError:
        print("Это не число! Попробуй снова.")
        continue  # Возвращаемся к запросу ввода, если не число

    attempts += 1  # Увеличиваем количество попыток

    if number < target_number:
        print("Загаданное число больше!")
    elif number > target_number:
        print("Загаданное число меньше!")
    else:
        print(f"Поздравляю! Вы угадали число {target_number} за {attempts} попыток!")
        break  # Выход из цикла, если число угадано

