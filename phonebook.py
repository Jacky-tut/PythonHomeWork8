import shutil

#Вывод меню
def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по имени\n"
          "3. Найти абонента по фамилии\n"
          "4. Найти абонента по номеру телефона\n"
          "5. Добавить абонента в справочник\n"
          "6. Удалить абонента из справочника\n"
          "7. Изменить данные абонента в справочнике\n"
          "8. Сохранить справочник в формате txt\n"
          "9. Закончить работу")
    choice = int(input())
    return choice

#Перевод справочника из файла в список из словарей
def read_csv(filename):
    results = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, "r", encoding="utf-8") as data:
        for line in data:
            record = dict(zip(fields, line.strip().split(",")))
            results.append(record)
    return results

#Выполняем работу с телефонной книгой в зависимости от пункта меню
def work_with_phonebook():
    choice = show_menu()
    phonebook = read_csv("phonebook.csv")
    while (choice != 9):
        if choice == 1:
            show_phonebook(phonebook)
        elif choice == 2:
            show_phonebook(find_by_name(phonebook))
        elif choice == 3:
            show_phonebook(find_by_surname(phonebook))
        elif choice == 4:
            show_phonebook(find_by_number(phonebook))
        elif choice == 5:
            add_new_user(phonebook)
            write_csv("phonebook.csv", phonebook)
        elif choice == 6:
            delete_user(phonebook)
            rewrite_csv("phonebook.csv", phonebook)
        elif choice == 7:
            change_userdata(phonebook)
            rewrite_csv("phonebook.csv", phonebook)
        elif choice == 8:
            make_txt()
        choice = show_menu

#1 Отобразить весь справочник
def show_phonebook(phonebook):
    for elem in phonebook:
        for key in elem:
            print(f"{key}: {elem[key]}")
        print()

#2 Найти абонента по имени
def find_by_name(phonebook):
    name = input("Введите имя для поиска: ")
    results = []
    for elem in phonebook:
        if elem["Имя"] == name:
            results.append(elem)
    return results

#3 Найти абонента по фамилии
def find_by_surname(phonebook):
    surname = input("Введите фамилию для поиска: ")
    results = []
    for elem in phonebook:
        if elem["Фамилия"] == surname:
            results.append(elem)
    return results

#4 Найти абонента по номеру телефона
def find_by_number(phonebook):
    number = input("Введите номер телефона для поиска: ")
    results = []
    for elem in phonebook:
        if elem["Номер телефона"] == number:
            results.append(elem)
    return results

#5 Добавить абонента в справочник
def add_new_user(phonebook):
    record = dict()
    for key in phonebook[0].keys():
        record[key] = input(f"Введите {key}: ")
    phonebook.append(record)
    
def write_csv(filename, phonebook):
    with open(filename, "a", encoding="utf-8") as data:
        line = " "
        for value in phonebook[-1].values():
            line += value + ","
        data.write(f"{line[-1]}\n")
        
#6 Удалить абонента из справочника
def delete_user(phonebook):
    user = input("Введите данные абонента, которого необходимо удалить: ")
    for elem in phonebook:
        for value in elem.values():
            if value == user:
                phonebook.remove(elem)
    
def rewrite_csv(filename, phonebook):
    with open(filename, "w", encoding="utf-8") as data:
        for i in range(len(phonebook)):
            line = " "
            for value in phonebook[1].values():
                line += value + ","
            data.write(f"{line[-1]}\n")

#7 Изменить данные абонента в справочнике
def change_userdata(phonebook):
    user = input("Введите данные абонента, которого надо изменить: ")
    change_atr = input("Введите атрибут, который необходимо изменить: ")
    new_atr = input("Введите новое значение атрибута: ")
    for elem in phonebook:
        for value in elem.values():
            if value == user:
                elem[change_atr] = elem[change_atr].replace(elem[change_atr], new_atr)

#8 Сохранить справочник в текстовом формате
def make_txt():
    filename = input("Введите имя файла для сохранения: ")
    shutil.copyfile("phonebook.csv" f"{filename}.txt")
    
#9 Закончить работу


        
    
    