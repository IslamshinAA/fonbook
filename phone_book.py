import view

phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book

def add_contact():
    global phone_book
    contact = view.input_new_conact()
    phone_book.append(contact)

def remove_contact():
    global phone_book
    id = view.input_remove_conact()
    confirm = input(f'Вы точно хотите удалить контакт? {phone_book[id-1][0]}? (y/n)')
    if confirm.lower() == 'y':
        del_contact = phone_book.pop(id-1)

def change_contact():
    global phone_book
    id = view.input_change_contact()
    del_contact = phone_book.pop(id - 1)
    id = view.input_new_conact()
    phone_book.append(id)

def search_name():
    global phone_book
    name = view.input_search_name_contact()
    for id in range(len(phone_book)):
        if name in phone_book[id]:
            print(*phone_book[id])
            print()
    else:
        print("Контакта с таким именем не сущесетвует!")


