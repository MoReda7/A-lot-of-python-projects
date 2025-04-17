contacts = {}
def add_contact(name,number):
    contacts[name] = number
    print(f"{name} has been added to the contacts")

def remove_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} has been removed from the contacts")
    else:
        print(f"{name} is not in the contacts")
        
def search_contact(name):
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}")
    else:
        print(f"{name} is not in the contacts")

x = 0
while x == 0 :
    print("Contact Management System")
    print("1. Add a contact")
    print("2. Remove a contact")
    print("3. Search for a contact")
    print("4. View all contacts")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Thank you for using the Contact Management System")
        x = 1

    elif choice == 1:
        name = input("Enter the name: ")
        number = input("Enter the number: ")
        if name in contacts:
            print(f"{name} is already in the contacts")
        else:
            add_contact(name,number)

    elif choice == 2:
        name = input("Enter the name: ")
        if name in contacts:
            remove_contact(name)
        else:
            print(f"{name} is not in the contacts")

    elif choice == 3:
        name = input("Enter the name: ")
        search_contact(name)

    elif choice == 4:
        print("All contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

    else:
        print("Invalid choice")