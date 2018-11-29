# Мне и самому стыдно за этот код, но он вроде работает
email_list_lines = {} # Словарь: 'емайл':[номер_строки_начала_письма, ...]
with open('unix.mailbox') as file:

    line_number = 0   # Первый блок заполняет словарь email_list_lines
    for line in file:
        line_number += 1
        if line[:5] == 'From ':
            current_email = line[5:5 + line[5:].find(' ')]
            if current_email in email_list_lines.keys():
                email_list_lines.get(current_email).append(line_number)
            else:
                email_list_lines[current_email] = [line_number]

    list = []  # Список с номерами строк начала писем + номер последней строки
    for i in email_list_lines.keys(): # для вычисления длины каждого письма
        list.extend(email_list_lines[i])
    list.append(line_number)
    list.sort()

    for email in email_list_lines.keys(): # Третий блок записывает письма
        with open(str(email + '.mailbox'), 'w') as wfile:
            for line in email_list_lines[email]:
                len = list[list.index(line) + 1] - list[list.index(line)]
                # Длина ^ письма
                file.seek(0)
                for _ in range(line - 1): # Переход к нужной строке для записи
                    file.readline() # len строк в файл

                for _ in range(len): # Запись len строк в файл
                    a = file.readline()
                    wfile.write(a)
