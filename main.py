import sqlite3


def open_connection():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection: sqlite3.Connection, cursor: sqlite3.Cursor):
    cursor.close()
    connection.close()


def create_student(name, age, major):
    connection, cursor = open_connection()
    cursor.execute("INSERT into students (name, age, major) VALUES (?, ?, ?)", [name, age, major])
    connection.commit()
    close_connection(connection, cursor)


def create_course(name):
    connection, cursor = open_connection()
    cursor.execute("INSERT into courses (name) VALUES (?)", [name])
    connection.commit()
    close_connection(connection, cursor)


def students_to_courses(student_id, course_id):
    connection, cursor = open_connection()
    cursor.execute("INSERT into students_courses (student_id, course_id) VALUES (?, ?)", [student_id, course_id])
    connection.commit()
    close_connection(connection, cursor)


def get_all_students():
    connection, cursor = open_connection()
    students = cursor.execute("SELECT * FROM students").fetchall()
    close_connection(connection, cursor)
    return students


def get_all_courses():
    connection, cursor = open_connection()
    courses = cursor.execute("SELECT * FROM courses").fetchall()
    close_connection(connection, cursor)
    return courses


def show_students_to_courses():
    connection, cursor = open_connection()
    students_courses = cursor.execute("SELECT * FROM students_courses").fetchall()
    close_connection(connection, cursor)
    return students_courses


while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        name = input("Введіть ім'я студента: ")
        age = int(input("Скільки років: "))
        major = input("Введіть спеціальність: ")
        create_student(name, age, major)
        print("Студент успішно доданий!")

    elif choice == "2":
        course_name = input("Введіть назву курсу: ")
        create_course(course_name)
        print("Курс успішно доданий!")

    elif choice == "3":
        students = get_all_students()
        print("\nСписок студентів: ")
        for student in students:
            print(f"ID: {student[0]}, Ім'я: {student[1]}, Вік: {student[2]}, Спеціальність: {student[3]}")

    elif choice == "4":
        courses = get_all_courses()
        print("\nСписок курсів: ")
        for course in courses:
            print(f"ID: {course[0]}, Назва: {course[1]}")

    elif choice == "5":
        student_id = int(input("Введіть Id студента: "))
        course_id = int(input("Введіть Id курса: "))
        students_to_courses(student_id, course_id)
        print("Студент успішно зареєстрований на курс!")

    elif choice == "6":
        students_courses = show_students_to_courses()
        # students = get_all_students()
        print("\nСписок студентів на конкретному курсі")
        for sc in students_courses:
            print(f"Id: {sc[0]}, Student Id: {sc[1]}, Course Id: {sc[2]}")

    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")


