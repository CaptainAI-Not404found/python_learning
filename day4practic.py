# --- задача 1: Таблица умножения ---
print("Задача 1: Таблица умножения от 1 до 10\n")
for i in range (1, 11):
    for j in range (1, 11):
        print(f"{i}*{j} ={i*j}" )
    print("_"* 15)

# --- Задача 2: счетчик от пользователя ---
print("\nЗадача 2: Счётчик от пользователя\n")
n = int(input("Введи число: "))
for i in range (1, n+1):
    print(i)

# --- Задача 3: Бот - анкетирование ---
print("\nЗадача 3: Анкета\n")
name = input("Как тебя зовут?: ")
age = input ("Сколько тебе лет?: ")
like_python = input("Тебе нравиться Python?: ")

print("\n📝 Результат анкеты:")
print("Имя:", name)
print("Возраст", age)
print("Любит Python:", like_python)