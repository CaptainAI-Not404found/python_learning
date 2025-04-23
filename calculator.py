num1 = float(input("Веддите первое число: "))
num2 = float(input("Ведите второе число: "))
operation = input("Введите операцию: ")

while True:
    if operation == "сложение":
        print(f"Сумма: {num1 + num2}")
    elif operation == "вычитание":
        print(f"Разница: {num1 - num2}")
    elif operation == "умножение":
        print(f"Произведение: {num1 * num2}")
    elif operation == "деление" and num2 != 0:
        print(f"Деление: {num1 / num2}")
    else:
        print("Ошибка, на 0 делить нельзя.")
    break   
