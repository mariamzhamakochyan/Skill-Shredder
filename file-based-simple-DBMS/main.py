from db import initialize_database, add_record, read_all_records, update_record, delete_record

def print_records(records):
    for i, record in enumerate(records):
        print(f"Record {i + 1}: {record}")

if __name__ == "__main__":
    initialize_database()

    while True:
        print("\nSimple DBMS Menu:")
        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            age = input("Enter the age: ")
            record = [name, age]
            add_record(record)
            print("Record added successfully!")

        elif choice == "2":
            records = read_all_records()
            print_records(records)

        elif choice == "3":
            record_id = int(input("Enter the record number to update: ")) - 1
            name = input("Enter the updated name: ")
            age = input("Enter the updated age: ")
            updated_record = [name, age]
            if update_record(record_id, updated_record):
                print("Record updated successfully!")
            else:
                print("Invalid record number.")

        elif choice == "4":
            record_id = int(input("Enter the record number to delete: ")) - 1
            if delete_record(record_id):
                print("Record deleted successfully!")
            else:
                print("Invalid record number.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

