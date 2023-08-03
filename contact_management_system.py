import os
import json

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self, filename="contacts.txt"):
        self.contacts = []
        self.filename = filename

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")

    def search_contact(self, query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]

    def save_contacts_to_file(self):
        with open(self.filename, "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone_number},{contact.email},{contact.address}\n")

    def load_contacts_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    name, phone, email, address = line.strip().split(",")
                    self.add_contact(Contact(name, phone, email, address))

def main():
    contact_manager = ContactManager()
    contact_manager.load_contacts_from_file()

    while True:
        print("\nContact Management System")
        print("1. Add new contact")
        print("2. View all contacts")
        print("3. Search contact by name or phone number")
        print("4. Delete contact by name")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_manager.add_contact(contact)
            contact_manager.save_contacts_to_file()
            print("Contact added successfully!")

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            found_contacts = contact_manager.search_contact(query)
            if found_contacts:
                print("Found contacts:")
                for i, contact in enumerate(found_contacts, start=1):
                    print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("No contacts found.")

        elif choice == "4":
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
            contact_manager.save_contacts_to_file()
            print("Contact deleted successfully!")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
