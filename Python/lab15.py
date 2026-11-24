# Lab 15 - Student Information Management System

# 1. Initial Data Setup: Store at least 3 default students in a nested dictionary
students = {
    "101": {
        "Name": "Aarav Sharma",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Priya Singh",
        "Branch": "BCA Cyber",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Rohan Verma",
        "Branch": "BCA Data Science",
        "Semester": "1",
        "Marks": [76, 82, 80]
    }
}

# 2. Control Flow: Menu-driven loop using while True
while True:
    print("\n========================================")
    print("    STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("========================================")
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    
    # Prompt the user to choose an operation (1 to 7)
    choice = input("\nEnter your choice (1-7): ")
    
    if choice == '1':
        # 1. View All Students — Display all enrolled student records using .items()
        print("\n--- Enrolled Student Records ---")
        if not students:
            print("No student records found.")
        else:
            for roll_no, details in students.items():
                print(f"Roll No: {roll_no} | Name: {details['Name']} | Branch: {details['Branch']} | Semester: {details['Semester']} | Marks: {details['Marks']}")
            print(f"Total Enrolled Students: {len(students)}")
            
    elif choice == '2':
        # 2. Search Student by Roll Number — Perform safe record lookup using .get()
        print("\n--- Search Student by Roll Number ---")
        roll_no = input("Enter Roll Number to search: ")
        student = students.get(roll_no)
        if student:
            print(f"\n[FOUND] Record for Roll No {roll_no}:")
            print(f"  Name     : {student['Name']}")
            print(f"  Branch   : {student['Branch']}")
            print(f"  Semester : {student['Semester']}")
            print(f"  Marks    : {student['Marks']}")
        else:
            print(f"[ERROR] Student with Roll Number {roll_no} not found.")
            
    elif choice == '3':
        # 3. Register New Student — Add a new student record ensuring unique Roll Number validation[cite: 16]
        print("\n--- Register New Student ---")
        roll_no = input("Enter Roll Number: ")
        if roll_no in students:
            print(f"[ERROR] Roll Number {roll_no} already exists.")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch: ")
            semester = input("Enter Semester: ")
            print("Enter marks obtained in 3 subjects:")
            m1 = int(input("  Subject 1: "))
            m2 = int(input("  Subject 2: "))
            m3 = int(input("  Subject 3: "))
            
            students[roll_no] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": [m1, m2, m3]
            }
            print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll_no}) registered successfully.")
            
    elif choice == '4':
        # 4. Update Student Details — Modify existing student attributes like Branch or Semester[cite: 16]
        print("\n--- Update Student Details ---")
        roll_no = input("Enter Roll Number to update: ")
        student = students.get(roll_no)
        if student:
            print(f"Current Details -> Name: {student['Name']}, Branch: {student['Branch']}, Semester: {student['Semester']}")
            print("1. Update Branch")
            print("2. Update Semester")
            up_choice = input("Choose attribute to update (1-2): ")
            if up_choice == '1':
                new_branch = input("Enter new branch: ")
                student['Branch'] = new_branch
                print("[SUCCESS] Branch updated successfully.")
            elif up_choice == '2':
                new_sem = input("Enter new semester: ")
                student['Semester'] = new_sem
                print("[SUCCESS] Semester updated successfully.")
            else:
                print("[ERROR] Invalid update option.")
        else:
            print(f"[ERROR] Student with Roll Number {roll_no} not found.")
            
    elif choice == '5':
        # 5. View Academic Performance — Calculate Total Marks, Percentage, Average, and Result status[cite: 16]
        print("\n--- View Academic Performance ---")
        roll_no = input("Enter Roll Number: ")
        student = students.get(roll_no)
        if student:
            marks = student['Marks']
            total_marks = sum(marks)
            max_possible = len(marks) * 100
            percentage = (total_marks / max_possible) * 100
            average = total_marks / len(marks)
            result = "PASS" if all(m >= 40 for m in marks) else "FAIL"
            
            print(f"\n--- Academic Report for Roll No {roll_no} ---")
            print(f"Name         : {student['Name']}")
            print(f"Total Marks  : {total_marks} / {max_possible}")
            print(f"Average Marks: {average:.2f}")
            print(f"Percentage   : {percentage:.2f}%")
            print(f"Result       : {result}")
        else:
            print(f"[ERROR] Student with Roll Number {roll_no} not found.")
            
    elif choice == '6':
        # 6. Delete Student Record — Safely remove a student record using .pop()[cite: 16]
        print("\n--- Delete Student Record ---")
        roll_no = input("Enter Roll Number to delete: ")
        removed = students.pop(roll_no, None)
        if removed:
            print(f"[SUCCESS] Student record for Roll No {roll_no} removed successfully.")
        else:
            print(f"[ERROR] Student with Roll Number {roll_no} not found.")
            
    elif choice == '7':
        # 7. Exit — Terminate the program cleanly[cite: 16]
        print("Exiting Student Information System. Goodbye!")
        break
        
    else:
        # Invalid choice error handling outside range 1-7[cite: 16]
        print("[ERROR] Invalid choice. Please enter a number between 1 and 7.")