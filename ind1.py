#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def add_record(phonebook, last_name, first_name, phone_number, birth_date):
    record = {
        'фамилия': last_name,
        'имя': first_name,
        'номер телефона': phone_number,
        'дата рождения': birth_date
    }
    phonebook.append(record)
    phonebook.sort(key=lambda x: x['номер телефона'][:3])  # Сортировка по первым трем цифрам номера телефона

def display_record(phonebook, last_name):
    for record in phonebook:
        if record['фамилия'] == last_name:
            print(f"Фамилия: {record['фамилия']}")
            print(f"Имя: {record['имя']}")
            print(f"Номер телефона: {record['номер телефона']}")
            print(f"Дата рождения: {'.'.join(map(str, record['дата рождения']))}")
            return
    print(f"Запись с фамилией '{last_name}' не найдена.")

def main():
    phonebook = []
    
    while True:
        print("\n1. Добавить запись")
        print("2. Найти запись по фамилии")
        print("3. Выйти")
        
        choice = input("Выберите действие (1/2/3): ")
        
        if choice == '1':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            phone_number = input("Введите номер телефона: ")
            birth_date = list(map(int, input("Введите дату рождения через пробел (дд мм гггг): ").split()))
            
            add_record(phonebook, last_name, first_name, phone_number, birth_date)
            print("Запись добавлена успешно.")
            
        elif choice == '2':
            last_name = input("Введите фамилию для поиска: ")
            display_record(phonebook, last_name)
            
        elif choice == '3':
            break
            
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()
