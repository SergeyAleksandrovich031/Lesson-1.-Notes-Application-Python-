import csv
from data_create import header_data, body_data, id_data, current_datetime


def input_data():
    note_id = id_data()
    header = header_data()
    body = body_data()
    now = current_datetime()

    with open('notes.csv', 'a', encoding='utf-8') as f:
        f.write(f"ID заметки: {note_id}; Заголовок: {header}; Текст: {body}; Дата/время создания(изменения): {now} \n")

    print("Заметка успешно сохранена")


def print_all_notes():
    with open('notes.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        print(*data, sep='')


def change_data():
    k, id_list = number_ID()
    if str(k) in id_list:
        ind = id_list.index(str(k))
        input_data()
        with open('notes.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()
            change_line = data.pop()
            data_list = data[:ind] + [change_line] + data[(ind + 1):]
    else:
        print("Указанный Вами ID заметки не найден. Попробуйте ввести корректный номер.")
    with open('notes.csv', 'w', encoding='utf-8') as f:
        f.writelines(data_list)


def remove():
    k, id_list = number_ID()
    if str(k) in id_list:
        ind = id_list.index(str(k))
        with open('notes.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()
            data_list = data[:ind] + data[ind + 1:]
    else:
        print("Указанный Вами ID заметки не найден. Попробуйте ввести корректный номер.")
    with open('notes.csv', 'w', encoding='utf-8') as f:
        f.writelines(data_list)


def number_ID():
    k = int(input("Введите номер ID заметки: "))
    with open('notes.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        id_list = []
        for i in data:  # Создаем список значений id (id_list), находящихся в файле notes.csv
            data_list = i.split(' ')
            id_list.append(data_list[2][:-1])
    return k, id_list


def print_note():
    k, id_list = number_ID()
    if str(k) in id_list:
        ind = id_list.index(str(k))
        with open('notes.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()
            print(data[ind])
    else:
        print("Указанный Вами ID заметки не найден. Попробуйте ввести корректный номер.")


def print_date_selection():  # делаем выборку по дате
    with open('notes.csv', 'r', encoding='utf-8') as csv_file:
        search_value = input("Введите дату записи/изменения файла для поиска в формате DD-MM-YYYY: ")
        for row in csv_file:
            if search_value in row:
                print(row[:-1])
            else:
                print("Запись не найдена.")


