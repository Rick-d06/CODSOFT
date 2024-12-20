contacts = []

def display_menu():
    print("\n=== Contact Book Menu ===")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
    else:
        print(f"{'Name':<15} {'Phone':<15}")
        print("-" * 30)
        for contact in contacts:
            print(f"{contact['Name']:<15} {contact['Phone']:<15}")

def search_contact():
    print("\n--- Search Contact ---")
    query = input("Enter name or phone number to search: ")
    found_contacts = [c for c in contacts if query in c['Name'] or query in c['Phone']]

    if not found_contacts:
        print("No matching contacts found.")
    else:
        print(f"{'Name':<15} {'Phone':<15} {'Email':<25} {'Address':<20}")
        print("-" * 70)
        for contact in found_contacts:
            print(f"{contact['Name']:<15} {contact['Phone']:<15} {contact['Email']:<25} {contact['Address']:<20}")

def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['Name'] == name:
            print("Enter new details (leave blank to keep unchanged):")
            new_phone = input(f"New phone number (current: {contact['Phone']}): ") or contact['Phone']
            new_email = input(f"New email (current: {contact['Email']}): ") or contact['Email']
            new_address = input(f"New address (current: {contact['Address']}): ") or contact['Address']

            contact['Phone'] = new_phone
            contact['Email'] = new_email
            contact['Address'] = new_address
            print(f"Contact '{name}' updated successfully!")
            return
    print(f"Contact '{name}' not found.")

def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['Name'] == name:
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully!")
            return
    print(f"Contact '{name}' not found.")

def main():
    while True:
        display_menu()
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
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
