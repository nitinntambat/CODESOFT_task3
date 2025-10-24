# CONTACT BOOK APPLICATION

contacts = []  # List to store contact dictionaries

def add_contact():
    print("\n=== ADD NEW CONTACT ===")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print(f"\nContact '{name}' added successfully!")

def view_contacts():
    print("\n=== CONTACT LIST ===")
    if not contacts:
        print("No contacts found.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\n=== SEARCH CONTACT ===")
    query = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    print("\n=== UPDATE CONTACT ===")
    query = input("Enter name or phone number of contact to update: ")
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print(f"\nUpdating contact: {contact['name']}")
            contact['name'] = input("Enter new name (leave blank to keep current): ") or contact['name']
            contact['phone'] = input("Enter new phone (leave blank to keep current): ") or contact['phone']
            contact['email'] = input("Enter new email (leave blank to keep current): ") or contact['email']
            contact['address'] = input("Enter new address (leave blank to keep current): ") or contact['address']
            print("Contact updated successfully!")
            return
    print("No matching contact found.")

def delete_contact():
    print("\n=== DELETE CONTACT ===")
    query = input("Enter name or phone number of contact to delete: ")
    for i, contact in enumerate(contacts):
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            confirm = input(f"Are you sure you want to delete '{contact['name']}'? (y/n): ")
            if confirm.lower() == 'y':
                contacts.pop(i)
                print("Contact deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
    print("No matching contact found.")

def main():
    while True:
        print("\n====== CONTACT BOOK MENU ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
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
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main()
