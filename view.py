import phone_book as pb


def main_menu():

    print(' Выберите команду меню: ')
    print('1. Показать телефонную книгу: ')
    print('2. Загрузить телефонную книгу: ')
    print('3. Сохранить телефонную книгу: ')
    print('4. Добавить контакт: ')
    print('5. Изменить контакт : ')
    print('6. Удалить контакт: ')
    print('7. Найти контакт:  ')
    print('0. Выйти из приложения\n')
    return input_menu()


def input_menu():
    while True:
        try:
            choice = int(input('Введите пункт меню: '))
            if choice in range(1, 8) or choice == 0:
                return choice
            else:
                print('Такого пункт меню нет. Внимательнее, пожалуйста')
        except:
            print('Ошибка ввода.')


def print_phone_book():
    phone_book = pb.get_phone_book()
    if len(phone_book) < 1:
        print('Телефонная книга пуста или не загружена\n')
    else:
        for id, contact in enumerate(phone_book, 1):
            print()
            print(id, *contact)
        print()

def input_new_conact():
    name = input("Введите имя контакта: ")
    phone = input('Введите телефон контакта: ')
    comment = input('Введите коментарий для контакта ')
    new_contact = [name, phone, comment]
    return new_contact

def input_remove_conact():
    print()
    print_phone_book()
    id = int(input("Введите id контакта, который стоит удалить:  "))
    return id