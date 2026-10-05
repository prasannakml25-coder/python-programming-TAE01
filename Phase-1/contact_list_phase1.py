contacts = []

def add_contact():
    name = input("Enter name: ")
    mobile = input("Enter mobile number: ")
    email = input("Enter email: ")
    organization = input("Enter organization: ")

    contact = {
        "name": name,
        "mobile": mobile,
        "email": email,
        "organization": organization
    }

    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name:", contact["name"])
        print("Mobile:", contact["mobile"])
        print("Email:", contact["email"])
        print("Organization:", contact["organization"])


def search_contact():
    keyword = input("Enter name or mobile number to search: ").lower()

    found = False
    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["mobile"]:
            print("\nContact found:")
            print("Name:", contact["name"])
            print("Mobile:", contact["mobile"])
            print("Email:", contact["email"])
            print("Organization:", contact["organization"])
            found = True

    if not found:
        print("Contact not found.")


def delete_contact():
    mobile = input("Enter mobile number of contact to delete: ")

    for contact in contacts:
        if contact["mobile"] == mobile:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


def main():
    while True:
        print("\n===== CONTACT LIST MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
