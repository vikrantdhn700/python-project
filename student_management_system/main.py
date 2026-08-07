import students

def validate_age(age_str: str) -> int:
    try:
        age = int(age_str)
        if age <= 0 or age > 70:
            raise students.StudentException("Age must be between 1 and 70.")
        return age            
    except ValueError:
        raise students.StudentException("Invalid age input: Age must be a valid number.")

def print_menu() -> None:
    print("\n" + "="*35)
    print("  STUDENT MANAGEMENT SYSTEM")
    print("="*35)
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Exit")
    print("="*35)

def run_cli() -> None:
    print_menu()
    while True:        
        choice = input("Enter option (1-6): ").strip()

        try:
            if choice == "1":
                s_id = input("Enter Student ID: ").strip()
                if not s_id:
                    raise students.StudentException("Student ID cannot be empty.")
                name = input("Enter Name: ").strip().title()
                if not name:
                    raise students.StudentException("Student Name cannot be empty.")
                age = validate_age(input("Enter Age: ").strip())
                course = input("Enter Course: ").strip()
                if not course:
                    raise students.StudentException("Course cannot be empty.")

                students.add_student(s_id, name, age, course)
                print(f"Success: Student '{name}' added successfully.")

            elif choice == "2":
                s_id = input("Enter Student ID to remove: ").strip()
                removed = students.remove_student(s_id)
                print(f"Success: Removed student '{removed['name']}' (ID: {s_id}).")

            elif choice == "3":
                s_id = input("Enter Student ID to update: ").strip()
                students.search_student(s_id)
                
                print("Leave blank if you do not want to change a field.")
                name = input("Enter New Name: ").strip().title()
                age_str = input("Enter New Age: ").strip()
                course = input("Enter New Course: ").strip()

                age = validate_age(age_str) if age_str else None
                name = name if name else None
                course = course if course else None

                students.update_student(s_id, name, age, course)  # type: ignore[arg-type]
                print(f"Success: Student ID '{s_id}' updated successfully.")

            elif choice == "4":
                s_id = input("Enter Student ID to search: ").strip()
                student = students.search_student(s_id)
                print("\n--- Student Details ---")
                print(f"ID     : {student['id']}")
                print(f"Name   : {student['name']}")
                print(f"Age    : {student['age']}")
                print(f"Course : {student['course']}")

            elif choice == "5":
                student_list = students.get_all_students()
                if not student_list:
                    print("\nNo student records found.")
                else:
                    print("\n" + "-"*50)
                    print(f"{'ID':<10} | {'Name':<20} | {'Age':<5} | {'Course':<10}")
                    print("-" * 50)
                    for s in student_list:
                        print(f"{s['id']:<10} | {s['name']:<20} | {s['age']:<5} | {s['course']:<10}")
                    print("-" * 50)

            elif choice == "6":
                print("Exiting application. Goodbye!")
                break
            else:
                print("Error: Invalid choice. Select from 1 to 6.")

        except students.StudentException as err:
            print(f"Operational Error: {err}")
        except Exception as err:
            print(f"Unexpected Error: {err}")

if __name__ == "__main__":
    run_cli()