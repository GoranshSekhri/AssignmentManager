assignments = []


def add_assignment():
    subject = input("Enter subject: ")
    title = input("Enter assignment title: ")
    deadline = input("Enter deadline (DD-MM-YYYY): ")

    assignment = {
        "subject": subject,
        "title": title,
        "deadline": deadline,
        "status": "Pending"
    }

    assignments.append(assignment)
    print("Assignment added successfully!")


def view_assignments():
    if len(assignments) == 0:
        print("No assignments available.")
    else:
        for i, assignment in enumerate(assignments, start=1):
            print("\nAssignment", i)
            print("Subject:", assignment["subject"])
            print("Title:", assignment["title"])
            print("Deadline:", assignment["deadline"])
            print("Status:", assignment["status"])


def mark_submitted():
    if len(assignments) == 0:
        print("No assignments available.")
        return

    view_assignments()

    try:
        number = int(input("\nEnter assignment number: "))

        if number >= 1 and number <= len(assignments):
            assignments[number - 1]["status"] = "Submitted"
            print("Assignment marked as submitted!")
        else:
            print("Invalid assignment number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n===== ASSIGNMENT MANAGER =====")
    print("1. Add Assignment")
    print("2. View Assignments")
    print("3. Mark Assignment as Submitted")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_assignment()

    elif choice == "2":
        view_assignments()

    elif choice == "3":
        mark_submitted()

    elif choice == "4":
        print("Thank you for using Assignment Manager!")
        break

    else:
        print("Invalid choice. Please try again.")