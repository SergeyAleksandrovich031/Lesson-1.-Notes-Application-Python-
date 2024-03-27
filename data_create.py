from datetime import datetime


def id_data():
    try:
        with open('id.txt', 'r+') as file:
            current_id = int(file.read().strip())
            file.seek(0)
            file.write(str(current_id + 1))
    except FileNotFoundError:
        with open('id.txt', 'w') as file:
            current_id = 0
            file.write('1')
    return current_id


def header_data():
    header = input("Введите название Вашей заметки: ")
    return header


def body_data():
    body = input("Введите текст Вашей заметки: ")
    return body


def current_datetime():
    now = datetime.now()
    formatted_date = now.strftime("%d-%m-%Y/%H:%M:%S")
    return formatted_date
