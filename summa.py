total = 0

while True:
    try:
        number = int(input("Введите число: "))
        total += number
    except ValueError:
        print("Пожалуйста, введите корректное число.")
    except KeyboardInterrupt:
        print("\nВыход из программы.")
        break
    finally:
        print(f"Текущая сумма: {total}")