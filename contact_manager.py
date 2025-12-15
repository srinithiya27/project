# contact_manager.py

contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"✅ Added {name} with phone {phone}")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContacts List:")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"🗑 Deleted contact {name}")
    else:
        print(f"No contact found with name {name}")

# Main loop
while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
