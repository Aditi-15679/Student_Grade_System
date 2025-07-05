"""
Dictionary

collection - key+value = pair =data1

left-side = key
right-side = value
{key1:value1 , key2:value2}

"""

#StudentGradeSystem 
"""
add
update
delete
view
exit

"""
"""
#create a dictionary
student={
    'Aditi':100,
    'Priya':200
}

#Accessing a element
print(student['Priya'])

#Update 
student['Priya'] = 400
print(student)

#delete
del student['Priya']
print(student)

"""

#Code
#Initialising dictionary
student_grades = { }

#Add a new student
def add_student(name, grade):
    student_grades[name] = grade
    # [riya] = 500
    print(f"Added{name} with a {grade}")
    # Added riya with a 500


#Update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        #riya = 500
        print(f"{name} with marks are updated {grade}")

    else:
        print(f"{name} is not found!")


#Delete  a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully  deleted")
    else:
        print(f"{name} is not found")

#View all students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No students found/added")



#Main Program
def main():
    while True:
        print('\n Student Grades Management System')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter your choice ="))
        if choice == 1:
            name = input("Enter student name  ")
            grade = int(input("Enter Student grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name =")
            grade = int(input("Enter student grade ="))
            update_student(name, grade)
        
        elif choice == 3:
            name = input("Enter student name =")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice")


main()