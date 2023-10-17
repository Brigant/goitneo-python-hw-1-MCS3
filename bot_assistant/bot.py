"""
Module providing a function of bot assistan.
This bot can store the contact in RAM using command "add [name] [phone]". 
There is a possibilyty to change existen user using command "change [name] [phone]". 
You can show a number of specified user by the command "phone [name]" and you can see all 
contacs using command "all".
"""


def is_validate_phone(phone) -> bool:
    """Phone validation function"""
    try:
        int(phone)
    except ValueError:
        return False

    return True


def parse_input(user_input):
    """The function parse user input and return command and arguments"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def add_contact(args, contacts):
    """The function add new contact to the contacts list"""
    if len(args) != 2:
        return "Wrong number of arguments"
    name, phone = args

    if not is_validate_phone(phone):
        return "Wrong phone number"
    elif name in contacts:
        return f"User {name} already exists"
    contacts[name] = phone

    return "Contact added."


def change_contact(args, contacts):
    """The function change existen contact"""
    if len(args) != 2:
        return "Wrong number of arguments"

    name, phone = args

    if not is_validate_phone(phone):
        return "Wrong phone number"

    if name not in contacts:
        return f"User {name} not found"
    contacts[name] = phone

    return "Contact updated."


def show_phone(args, contacts):
    """The function show phone number of the contact"""
    if len(args) == 1:
        name = args[0]

    try:
        return contacts[name]
    except KeyError:
        return f"User {name} not found"


def shaw_all(contacts):
    """The function show all contacts"""
    for name in contacts:
        print(f'{name} {contacts[name]}')


def main():
    """The main function"""
    contacts = dict()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if len(user_input)>0:  
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                print(add_contact(args, contacts))

            elif command == "change":
                print(change_contact(args, contacts))

            elif command == "phone":
                print(show_phone(args, contacts))

            elif command == "all":
                shaw_all(contacts)

            else:
                print("Invalid command.")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
