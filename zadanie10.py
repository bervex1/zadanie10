from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name_value):
        self.name = Name(name_value)
        self.phones = []

    def add_phone(self, phone_value):
        phone = Phone(phone_value)
        self.phones.append(phone)

    def remove_phone(self, phone_value):
        for phone in self.phones:
            if phone.value == phone_value:
                self.phones.remove(phone)
                break

    def edit_phone(self, old_phone_value, new_phone_value):
        for phone in self.phones:
            if phone.value == old_phone_value:
                phone.value = new_phone_value
                break

    def __str__(self):
        phones_str = ', '.join(str(phone) for phone in self.phones)
        return f"Name: {self.name}, Phones: {phones_str}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def search_records(self, criteria):
        results = []
        for record in self.data.values():
            match = True
            for field, value in criteria.items():
                if field == 'name' and record.name.value != value:
                    match = False
                    break
                elif field == 'phone':
                    phone_match = any(phone.value == value for phone in record.phones)
                    if not phone_match:
                        match = False
                        break
            if match:
                results.append(record)
        return results


def main():
    address_book = AddressBook()

    while True:
        command = input("Enter a command: ").lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            _, name, phone = command.split()
            if name not in address_book.data:
                record = Record(name)
                record.add_phone(phone)
                address_book.add_record(record)
                print(f"Contact {name} with phone {phone} added.")
            else:
                print(f"Contact {name} already exists. Use 'edit' to modify.")
        elif command.startswith("edit"):
            _, name, old_phone, new_phone = command.split()
            if name in address_book.data:
                record = address_book.data[name]
                record.edit_phone(old_phone, new_phone)
                print(f"Phone number for {name} changed to {new_phone}.")
            else:
                print(f"Contact {name} not found.")
        elif command.startswith("search"):
            _, field, value = command.split()
            criteria = {field: value}
            results = address_book.search_records(criteria)
            if results:
                for result in results:
                    print(result)
            else:
                print("No matching contacts found.")
        elif command == "show all":
            for record in address_book.data.values():
                print(record)
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
