from logger import input_data, print_all_notes, change_data, remove, print_note, print_date_selection


def interface():
    print(
        "Добрый день! Вы запустили приложение 'Заметки'. В программе используются следующие команды:"
        "\n 1 - создание заметки \n 2 - вывод всех заметок \n 3 - вывод заметки (по номеру ID) \n 4 - изменение заметки" 
        "\n 5 - удаление заметки, \n 6 - выборка заметок по дате")
    command = input("Введите число: ")

    while command not in ('1', '2', '3', '4', '5', '6'):
        print("Неправильный ввод")
        command = input("Введите число: ")

    if command == "1":
        input_data()
    elif command == "2":
        print_all_notes()
    elif command == "3":
        print_note()
    elif command == "4":
        change_data()
    elif command == "5":
        remove()
    elif command == "6":
        print_date_selection()
