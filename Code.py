from my_classes import Name,Phone, AddressBook

contacts = AddressBook{}  # added missing dictionary declaration

# decorator
def input_error(func):
    def inner(*args):  # modified to accept variable number of arguments
        try:
            result = func(*args)  # modified to pass variable number of arguments
            return result
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Please give me name and phone number separated by space"
        except IndexError:
            return "Please provide name or name and phone number separated by space"
    return inner

def exit_test(*args):  # modified to accept variable number of arguments
    return 

def hello_users(*args):  # modified to accept variable number of arguments
    print("How can I help you?")

@input_error
def add_contact(name, phone):  # modified to accept variable number of arguments
    name = Name(name)
    phone = Phone(phone)
    contacts.add_record(Record(name))
    contacts[name].add_phone(phone)
    return f"{name.value}'s phone number {phone.value} added"  # modified to access the value attribute

def unknown_command(*args):  # modified to accept variable number of arguments
    print('Unknown command')

@input_error
def change_contact(name, phone):  # modified to accept variable number of arguments
    name = Name(name)
    phone = Phone(phone)
    old_phone = contacts[name].phones[0]
    contacts[name].phones[0] = phone
    return f"{name.value}'s old phone number {old_phone.value} changed to {phone.value}"  # modified to access the value attribute

def show_phone(name):  # modified to accept a single argument
    name = Name(name)
    if not contacts:
        return "No contacts found"
    phone = contacts.get(name.value)
    if phone:
        return f'Name {name.value}: phone {phone.phones[0].value}'  # modified to access the value attribute
    return "Contact not found"

def show_all(name, phone):  # modified to accept variable number of arguments
    name = Name(name)
    phone = Phone(phone)
    if not contacts:
        return "No contacts found"
    result = ''
    for name, record in contacts.items():
        phone = record.phones[0]
        result += f'Name {name}: phone {phone.value} \n'
    return result

HANDLERS = {
    'hello': hello_users,
    'add': add_contact,
    'change': change_contact,
    'show all': show_all,
    'exit': exit_test,
    'goodbye': exit_test,
    'close': exit_test
}

def parse_input(user_input):
    command_name, name, phone = user_input.split()
    command_name = command_name.lstrip()

    try:
        handler = HANDLERS[command_name.lower()]
    except KeyError:
        if args:
            command_name = command_name + ' ' + args[0]
            args = args[1:]
        handler = HANDLERS.get(command_name.lower(), unknown_command)
    return handler, name, phone

def main():
    while True:
    
        print('Please input command, name and phone. For example: add Lesia 033-332-2233')
        user_input = input('')
        handler, name, phone = parse_input(user_input)
        result = handler(name, phone)
        if not result:
            print('input true args')  # corrected typo
            break
        print(result)

if __name__ == "__main__":
    main()
