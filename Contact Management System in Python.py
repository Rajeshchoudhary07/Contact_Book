# Contact Management System
contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter home address: ")
    
    if name in contacts:
        print(f"Contact with name {name} already exists!")
    else:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact {name} added successfully.")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts found!")

def search_contact():
    search = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search == name or search == details['phone']:
            print(f"\nContact found: {name}")
            print(f"Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
            break
    if not found:
        print("Contact not found!")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating contact {name}. Leave field empty if no change.")
        phone = input(f"Current phone: {contacts[name]['phone']}, New phone: ")
        email = input(f"Current email: {contacts[name]['email']}, New email: ")
        address = input(f"Current address: {contacts[name]['address']}, New address: ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found!")

def contact_manager():
    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

# Run the contact manager
contact_manager()
