task_choice = input("Введіть номер завдання (1: Вікові групи користувачів або 2: Конвертація числа): ")

if task_choice == '1':
    users_age_group = {
        "Олександр": "20-29",
        "Марія": "30-39",
        "Іван": "40-49",
        "Ольга": "50-59",
    }

    user_name = input("Введіть ім'я користувача: ")

    if user_name in users_age_group:
        print(f"Вікова група користувача {user_name}: {users_age_group[user_name]}")
    else:
        print("Користувача з таким іменем не знайдено.")
elif task_choice == '2':
    user_input = input("Введіть число: ")

    try:
        float_number = float(user_input)
        rounded_number = round(float_number)
        print(f"Число {float_number} було конвертовано в ціле число: {rounded_number}")
    except ValueError:
        print("Помилка: введені дані не можна конвертувати в число.")
else:
    print("Невірний вибір завдання. Будь ласка, введіть 1 або 2.")
