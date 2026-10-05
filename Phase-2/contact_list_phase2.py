import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter mobile number: ").strip()
    email = input("Enter email: ").strip()
    organization = input("Enter organization: ").strip()

    if not name or not phone:
        print("Name and mobile number are required.")
        return

    if any(contact["phone"] == phone for contact in contacts):
        print("A contact with this mobile number already exists.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "organization": organization
    })
    save_contacts(contacts)
    print("Contact added and saved successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name:", contact["name"])
        print("Mobile:", contact["phone"])
        print("Email:", contact["email"])
        print("Organization:", contact["organization"])

def search_contact(contacts):
    keyword = input("Enter name or mobile number to search: ").strip().lower()
    found = False

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print("\nContact Found")
            print("Name:", contact["name"])
            print("Mobile:", contact["phone"])
            print("Email:", contact["email"])
            print("Organization:", contact["organization"])
            found = True

    if not found:
        print("Contact not found.")

def update_contact(contacts):
    phone = input("Enter mobile number of contact to update: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            print("Leave a field blank to keep the existing value.")

            name = input(f"Name [{contact['name']}]: ").strip()
            email = input(f"Email [{contact['email']}]: ").strip()
            organization = input(
                f"Organization [{contact['organization']}]: "
            ).strip()

            if name:
                contact["name"] = name
            if email:
                contact["email"] = email
            if organization:
                contact["organization"] = organization

            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")

def delete_contact(contacts):
    phone = input("Enter mobile number of contact to delete: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n===== Contact List Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
