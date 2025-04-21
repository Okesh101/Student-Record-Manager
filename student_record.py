# The code below is a simple student record management system that allows you to add, view, search, and delete student records.
# It was created by Okesh

student_record = {}

def add_student():
    name = input("Enter Student name as key: ")
    age = int(input("Enter Student age: "))
    percentage = input("Enter Student percentage score: ")

    student_record[name] = [age, percentage]
    print(f"Student {name} added successfully.")

def view_all_students():
    count = 1
    print("Here are the details of all students:")
    for student in student_record:
        print(f"\nStudent {count}...")
        print("Details: ")
        print("Name:", student)
        print("Age:", student_record[student][0])
        print("Percentage score:", student_record[student][1])
        count += 1


def search_student():
    name = input("Enter Student name to search: ")
    if name in student_record:
        print("\nStudent found.")
        print("Details: ")
        print("Name:", name)
        print("Age:", student_record[name][0])
        print("Percentage score:", student_record[name][1])
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter Student name to delete: ")
    if name in student_record:
        del student_record[name]
        print(f"Student {name} deleted successfully.")
    else:
        print(f"Student {name} not found.")

print("Welcome to Student Records Manager.")
print("Choose what you want to do today")
print("1. Add Student" \
      "\n2. View All Students" \
      "\n3. Search for a Student" \
      "\n4. Delete a student" \
      "\n5. Delete all students" \
      "\n6. Exit")

while True:
    choice = input("\nEnter your choice (1-6): ")
    if choice == "1":
        print("You chose to add a student.")
        print("Please enter the following details:")
        add_student()
    elif choice == "2":
        print("You chose to view all students.")
        if (len(student_record) == 0):
            print("There are no students found in the record manager.")
        else:
            view_all_students()
    elif choice == "3":
        print("You chose to search for a student.")
        search_student()
    elif choice == "4":
        print("You chose to delete a student.")
        delete_student()
    elif choice == "5":
        print("You chose to delete all students.")
        if (len(student_record) == 0):
            print("There are no students found in the record manager.")
        else:
            print("Deleting all students...")
            student_record.clear()
            print("\nAll students deleted successfully.")
    elif choice == "6":
        print("You chose to exit the program.")
        print("Thank you for using Student Records Manager.")
        break
    else:
        print("Invalid choice. Please try again.")
    
    cont = input("\nDo you want to continue? (yes/no): ")
    if cont.lower() == "no":
        print("Thank you for using Student Records Manager.")
        break
    elif cont.lower() == "yes":
        continue
    else:
        print("Invalid input.")
        print("Thank you for using Student Records Manager.")
        break
