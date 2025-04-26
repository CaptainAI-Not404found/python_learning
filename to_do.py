tasks = []

def show_tasks():
    if not tasks:
        print("Список пуст.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    
def add_task():
    task = input("Введите задачу: ")
    tasks.append(task)
    print("Задача добавлена")

def remove_task():
    if not tasks:  # Проверяем, пуст ли список
        print("Нет задач для удаления.")
        return
    
    show_tasks()  # Показываем задачи перед удалением
    try:
        task_num = int(input("Введите номер задачи для удаления: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Задача '{removed_task}' удалена.")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

while True:
    print("\n1. Посмотреть задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выйти")
    choice = input("Выберите операцию: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        break
    else:
        print("Неверный выбор.")
