students = []

def load_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")
                students.append({"Roll": roll, "Name": name, "Marks": marks})
    except FileNotFoundError:
        pass

def save_students():
    with open("students.txt", "w") as file:
        for s in students:
            file.write(f"{s['Roll']},{s['Name']},{s['Marks']}\n")

load_students()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        students.append({"Roll": roll, "Name": name, "Marks": marks})
        save_students()
        print("Student Added Successfully!")

    elif choice == "2":
        if students:
            for s in students:
                print(s)
        else:
            print("No Records Found")

    elif choice == "3":
        roll = input("Enter Roll No: ")
        found = False
        for s in students:
            if s["Roll"] == roll:
                print(s)
                found = True
                break
        if not found:
            print("Student Not Found")

    elif choice == "4":
        roll = input("Enter Roll No: ")
        found = False
        for s in students:
            if s["Roll"] == roll:
                s["Name"] = input("Enter New Name: ")
                s["Marks"] = input("Enter New Marks: ")
                save_students()
                print("Student Updated Successfully!")
                found = True
                break
        if not found:
            print("Student Not Found")

    elif choice == "5":
        roll = input("Enter Roll No: ")
        found = False
        for s in students:
            if s["Roll"] == roll:
                students.remove(s)
                save_students()
                print("Student Deleted Successfully!")
                found = True
                break
        if not found:
            print("Student Not Found")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")