def parse_input(user_input):
    """
    Розбирає введений користувачем рядок на команду та її аргументи.

    param user_input: Введений користувачем рядок.
    return: Команда та список її аргументів.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Додає новий контакт у словник.

    param args: Список аргументів, який містить ім'я та номер телефону.
    param contacts: Словник збережених контактів.
    return: Рядок з повідомленням про результат додавання.
    """
    name, phone = args
    if name in contacts:
        return f"Введений контакт з ім'ям {name} вже існує."
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    """
    Змінює номер телефону існуючого контакту.

    param args: Список аргументів, який містить ім'я та новий номер телефону.
    param contacts: Словник збережених контактів.
    return: Рядок з повідомленням про результат зміни.
    """
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f'Контакт {name} змінено.'
    return 'Вказаного користувача не існує.'


def del_contact(args, contacts):
    """
    Видаляє контакт зі словника.

    param args: Список аргументів, який містить ім'я.
    param contacts: Словник збережених контактів.
    return: Рядок з повідомленням про результат видалення.
    """
    name, = args
    if name in contacts:
        del contacts[name]
        return f"Контакт {name} видалено"
    return f"Контакт {name} не знайдено"


def show_phone(args, contacts):
    """
    Відображає номер телефону за вказаним ім'ям.

    param args: Список аргументів, який містить ім'я.
    param contacts: Словник збережених контактів.
    return: Рядок з номером телефону або повідомленням про помилку.
    """
    name, = args
    if name in contacts:
        return f"{name}: {contacts[name]}"
    return f"Контакт {name} не знайдено."


def main():
    """
    Головна функція для управління циклом команд бота-помічника.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "all":
            print(contacts)
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "del":
            print(del_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()