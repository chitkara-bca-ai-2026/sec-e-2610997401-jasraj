# Lab 03 - Student Record Display

print("========================================")
print("          STUDENT RECORD DISPLAY")
print("========================================")

# 1. Take input from the user
student_name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))

# 2. Display the details in a formatted output
print()
print("----------------------------------------")
print("Student Details:")
print(f"Name   : {student_name}")
print(f"Age    : {age}")
print(f"Marks  : {marks}")
print("----------------------------------------")