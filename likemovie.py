films = []

while True:
    film = input("Добавь свой любимый фильм (или 'стоп' для завершения): ")
    if film.lower() == 'стоп':
        break
    films.append(film)
    print("Твой любимый фильм:", film)

print("\nСписок твоих любимых фильмов:")
for f in films:
    print("-", f)

# Удаление фильма
remove_film = input("\nКакой фильм удалить из списка? ")
if remove_film in films:
    films.remove(remove_film)
    print(f"Фильм '{remove_film}' удалён.")
else:
    print("Такого фильма нет в списке.")

# Добавление нового фильма
new_film = input("Добавь новый фильм: ")
films.append(new_film)
print(f"Фильм '{new_film}' добавлен.")

# Вывод списка в обратном порядке
print("\nТвой обновлённый список фильмов:")
for f in films[::-1]:
    print("-", f)
