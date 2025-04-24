bank = 0.0
history = []
while True:
    operation = input("Выберите операцию: доход/расход/баланс/история/выход\n")
    if operation == "доход":
        summa = float(input("Сколько получил: "))
        bank += summa
        print(f"Ваш баланс: {bank}")
        history.append(f"+{summa} доход")
    elif operation == "расход":
        summa = float(input("Сколько потратил: "))
        if summa <= bank:
            bank -= summa
            print(f"Ваш баланс: {bank}")
            history.append(f"-{summa} расход")
        else:
            print("Банк не может быть пустым.")
    elif operation == "баланс":
        print(f"Ваш баланс: {bank}")
    elif operation == "история":
        if history:
            for record in history:
                print(record)
        else:
            print("Ваша история пуста.")
    elif operation == "выход":
        print(f"Ваш баланс: {bank}")
        print("Выход из программы.")
        break
    else:
        print("Неизвестная операция. Побробуйте снова")