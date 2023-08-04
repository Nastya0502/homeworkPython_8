# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

import os

file_name = "tell.txt"

def load_tel():
    if os.path.isfile(file_name):
        with open(file_name, encoding="UTF-8") as f:
            r = f.readlines()
            s = []
            for line in r:
                s.append(line.split())
        return s
    s = []
    return s

def input_tel(s):
    first_name = input("Введите имя: ").capitalize()
    patronimic = input("Введите отчество: ").capitalize()
    last_name = input("Введите фамилию: ").capitalize()
    tel = input("Введите номер телефона: ").capitalize()
    with open(file_name, "a", encoding="UTF-8") as f:
        f.write(f"{last_name} {first_name} {patronimic} {tel} \n")
    s.append([last_name, first_name, patronimic, tel])
    return s

def search_tel(s, object):
    for line in s:
        if object in line or object.capitalize() in line:
            return " ".join(line)
    return "Запись не найдена"

def change_tel(s, object, data, new_data):
    for line in s:
        if object in line or object.capitalize() in line:
            if data==1:
                line[1] = new_data
            elif data==2:
                line[2] = new_data
            elif data==3:
                line[0] = new_data
            elif data==4:
                line[3] = new_data
            else:
                print("Напишите цифру от 1 до 4 из пункта меню.")
    return "Запись не найдена"

def delete_tel(s, object, delete_data):
    for line in s:
        if object in line or object.capitalize() in line:
            if delete_data==1:
                line.remove(line[1])
            elif delete_data==2:
                line.remove(line[2])
            elif delete_data==3:
                line.remove(line[0])
            elif delete_data==4:
                line.remove(line[3])
            else:
                print("Напишите цифру от 1 до 4 из пункта меню.")
    return "Запись не найдена"

def show_tell(s):
    for line in s:
        print(" ".join(line))


if __name__ == "__main__":
    s = load_tel()
    while True:
        action = input("1 - Добавить данные \n2 - Искать данные \n3 - Посмотреть справочник\n4 - Изменить запись\n5 - Удалить данные в записи\n6 - Выход:\n")
        if action == "1":
            s = input_tel(s)
        elif action == "2":
            search_name = input("Что вы хотите найти? ")
            print(search_tel(s, search_name))
        elif action == "3":
            show_tell(s)
        elif action == "4":
            search_name = input("Какую запись Вы хотите изменить? ")
            data = int(input("Какие данные Вы хотите изменить?\n1 - Имя\n2 - Отчество\n3 - Фамилия\n4 - Номер телефона\n"))
            new_data = input("Введите новые данные: ")
            change_tel(s, search_name, data, new_data)
        elif action == "5":
            delete_name = input("В какой записи Вы хотите удалить данные? ")
            delete_object = int(input("Какие данные Вы хотите удалить?\n1 - Имя\n2 - Отчество\n3 - Фамилия\n4 - Номер телефона\n"))
            delete_tel(s, delete_name, delete_object)
        elif action == "6":
            print("Good bye!")
            break
        else:
            print("Подумай!")