import sqlite3
from datetime import datetime

conn = sqlite3.connect("campus_companion.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS assignments(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
due_date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
amount REAL,
category TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS medicines(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
time TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
note TEXT
)
""")

conn.commit()

# Attendance
def attendance():
    attended = int(input("Classes Attended: "))
    total = int(input("Total Classes: "))

    percentage = (attended / total) * 100

    print(f"\nAttendance = {percentage:.2f}%")

    if percentage < 75:
        print("Warning: Attendance Shortage")
    else:
        print("Attendance Safe")

# Assignment
def add_assignment():
    title = input("Assignment Title: ")
    due = input("Due Date: ")

    cursor.execute(
        "INSERT INTO assignments(title,due_date) VALUES (?,?)",
        (title, due)
    )
    conn.commit()

    print("Assignment Added")

def view_assignments():
    data = cursor.execute(
        "SELECT * FROM assignments"
    )

    for row in data:
        print(row)

# Expense Tracker
def add_expense():
    amount = float(input("Amount: "))
    category = input("Category: ")

    cursor.execute(
        "INSERT INTO expenses(amount,category) VALUES (?,?)",
        (amount, category)
    )

    conn.commit()
    print("Expense Added")

def view_expenses():
    total = 0

    data = cursor.execute(
        "SELECT * FROM expenses"
    )

    for row in data:
        print(row)
        total += row[1]

    print("Total Expense =", total)

# Medicine Reminder
def add_medicine():
    name = input("Medicine Name: ")
    time = input("Time(HH:MM): ")

    cursor.execute(
        "INSERT INTO medicines(name,time) VALUES (?,?)",
        (name, time)
    )

    conn.commit()

    print("Medicine Added")

def medicine_reminder():
    current = datetime.now().strftime("%H:%M")

    data = cursor.execute(
        "SELECT * FROM medicines"
    )

    for row in data:
        if row[2] == current:
            print(f"\nREMINDER: Take {row[1]}")

# Notes Manager
def add_note():
    note = input("Write Note: ")

    cursor.execute(
        "INSERT INTO notes(note) VALUES (?)",
        (note,)
    )

    conn.commit()

    print("Note Saved")

def view_notes():
    data = cursor.execute(
        "SELECT * FROM notes"
    )

    for row in data:
        print(row)

# CGPA Calculator
def cgpa():
    semesters = int(input("Number of Semesters: "))

    total = 0

    for i in range(semesters):
        gpa = float(
            input(f"Semester {i+1} GPA: ")
        )

        total += gpa

    print(
        "CGPA =",
        round(total / semesters, 2)
    )

# Main Program
while True:

    medicine_reminder()

    print("\n====== CAMPUS COMPANION ======")
    print("1 Attendance Calculator")
    print("2 Add Assignment")
    print("3 View Assignments")
    print("4 Add Expense")
    print("5 View Expenses")
    print("6 Add Medicine")
    print("7 Add Note")
    print("8 View Notes")
    print("9 CGPA Calculator")
    print("10 Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        attendance()

    elif choice == "2":
        add_assignment()

    elif choice == "3":
        view_assignments()

    elif choice == "4":
        add_expense()

    elif choice == "5":
        view_expenses()

    elif choice == "6":
        add_medicine()

    elif choice == "7":
        add_note()

    elif choice == "8":
        view_notes()

    elif choice == "9":
        cgpa()

    elif choice == "10":
        conn.close()
        break

    else:
        print("Invalid Choice")