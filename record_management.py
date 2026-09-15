import csv

FILE_NAME = "records.csv"

print("===== Welcome to Console Record Management System by Deeya Mathur =====")


# Add Record
def add_record():
    print("\n----- Add Record -----")

    name = input("Enter Name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter Age: "))

        if age <= 0:
            print("Age must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid age.")
        return

    course = input("Enter Course: ").strip()

    if course == "":
        print("Course cannot be empty.")
        return

    email = input("Enter Email: ").strip()

    if "@" not in email or "." not in email:
        print("Please enter a valid email.")
        return

    try:
        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, course, email])

        print("Record added successfully!")

    except OSError:
        print("Error: Unable to save the record.")


# View Records
def view_record():
    print("\n----- View Records -----")

    found = False

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:

                if len(row) != 4:
                    continue

                print("-------------------------")
                print("Name   :", row[0])
                print("Age    :", row[1])
                print("Course :", row[2])
                print("Email  :", row[3])

                found = True

        if not found:
            print("No records found.")

    except FileNotFoundError:
        print("No records found.")

    except OSError:
        print("Error: Unable to read the records file.")


# Search Record
def search_record():
    print("\n----- Search Record -----")

    search_name = input("Enter Name to search: ").strip()

    if search_name == "":
        print("Please enter a name.")
        return

    found = False

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:

                if len(row) != 4:
                    continue

                if row[0].strip().lower() == search_name.lower():

                    print("\nRecord Found!")
                    print("Name   :", row[0])
                    print("Age    :", row[1])
                    print("Course :", row[2])
                    print("Email  :", row[3])

                    found = True

        if not found:
            print("Record not found.")

    except FileNotFoundError:
        print("No records found.")

    except OSError:
        print("Error: Unable to read the records file.")


# Update Record
def update_record():
    print("\n----- Update Record -----")

    search_name = input("Enter Name to update: ").strip()

    if search_name == "":
        print("Please enter a name.")
        return

    records = []

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:

                if len(row) == 4:
                    records.append(row)

    except FileNotFoundError:
        print("No records found.")
        return

    except OSError:
        print("Error: Unable to read the records file.")
        return

    found = False

    for row in records:

        if row[0].strip().lower() == search_name.lower():

            print("\nEnter new details:")

            new_name = input("Enter Name: ").strip()

            if new_name == "":
                print("Name cannot be empty.")
                return

            try:
                new_age = int(input("Enter Age: "))

                if new_age <= 0:
                    print("Age must be greater than 0.")
                    return

            except ValueError:
                print("Please enter a valid age.")
                return

            new_course = input("Enter Course: ").strip()

            if new_course == "":
                print("Course cannot be empty.")
                return

            new_email = input("Enter Email: ").strip()

            if "@" not in new_email or "." not in new_email:
                print("Please enter a valid email.")
                return

            row[0] = new_name
            row[1] = str(new_age)
            row[2] = new_course
            row[3] = new_email

            found = True
            break

    if not found:
        print("Record not found.")
        return

    try:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(records)

        print("Record updated successfully!")

    except OSError:
        print("Error: Unable to update the record.")


# Delete Record
def delete_record():
    print("\n----- Delete Record -----")

    search_name = input("Enter Name to delete: ").strip()

    if search_name == "":
        print("Please enter a name.")
        return

    records = []

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:

                if len(row) == 4:
                    records.append(row)

    except FileNotFoundError:
        print("No records found.")
        return

    except OSError:
        print("Error: Unable to read the records file.")
        return

    found = False

    for row in records:

        if row[0].strip().lower() == search_name.lower():
            records.remove(row)
            found = True
            break

    if not found:
        print("Record not found.")
        return

    try:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(records)

        print("Record deleted successfully!")

    except OSError:
        print("Error: Unable to delete the record.")


# Main Menu
while True:

    print("""
What would you like to do?

1. Add Record
2. View Record
3. Search Record
4. Update Record
5. Delete Record
6. Exit
""")

    try:
        n = int(input("Enter Number: "))

    except ValueError:
        print("Please enter a number from 1 to 6.")
        continue

    if n == 1:
        add_record()

    elif n == 2:
        view_record()

    elif n == 3:
        search_record()

    elif n == 4:
        update_record()

    elif n == 5:
        delete_record()

    elif n == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")