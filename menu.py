import data_base
import view
import phone_book



def choice_menu(choice):
    match choice:
        case 1:
            view.print_phone_book()
        case 2:
            data_base.load_contacts()
        case 3:
            data_base.save_contacts()
        case 4:
            phone_book.add_contact()
        case 5:
            pass
        case 6:
            phone_book.remove_contact()
        case 7:
            pass
        case 0:
            return True

while True:
    choice = view.main_menu()
    if choice_menu(choice):
        break