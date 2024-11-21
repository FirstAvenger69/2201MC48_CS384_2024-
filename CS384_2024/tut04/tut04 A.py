def add_student(students, name, grades):
    name = name.lower()
    if name in students:
        print(f"Student {name} already exists. Use update_student to add grades.")
    else:
        students[name] = grades
        print(f"Student {name} added successfully.")

def update_student(students, name, grades):
    name = name.lower()
    if name in students:
        
        
        students[name].extend(grades)
        print(f"Grades updated for student {name}.")
    else:
        print(f"Student {name} does not exist. Use add_student to add the student.")

def calculate_average(students):
    averages = {}
    for name, grades in students.items():
        averages[name] = sum(grades) / len(grades)
    return averages

def print_students(students):
    averages = calculate_average(students)
    for name, avg in averages.items():
        print(f"{name.capitalize()} - Average: {avg:.2f}")

def sort_students_by_grades(students):
    averages = calculate_average(students)
    sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    return sorted_students

def main():
    students = {}

    while True:
        print("\nChoose an option:")
        print("1. Add a new student with grades")
        print("2. Update grades of an existing student")
        print("3. Print all students with their average grades")
        print("4. Sort students by their grades in descending order")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the student's name: ")
            grades = list(map(int, input("Enter the student's grades separated by space: ").split()))
            add_student(students, name, grades)

        elif choice == 2:
            name = input("Enter the student's name: ")
            grades = list(map(int, input("Enter the new grades separated by space: ").split()))
            update_student(students, name, grades)

        elif choice == 3:
            print_students(students)

        elif choice == 4:
            sorted_students = sort_students_by_grades(students)
            for name, avg in sorted_students:
                print(f"{name.capitalize()} - Average: {avg:.2f}")

        elif choice == 5:
            break

        else:
            print("Invalid choice. Please try again.")

main()