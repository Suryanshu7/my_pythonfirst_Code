"""
Module 6: Data Structures and Strings in Python
Task 1: Create a Dictionary of Student Marks
Problem Statement: Write a Python program that:
    1.Creates a dictionary where student names are keys and their marks are values.
    2.Asks the user to input a student's name.
    3.Retrieves and displays the corresponding marks.
    4.If the student’s name is not found, display an appropriate message.

"""

student_dict = {
    'student_1' : {
        "name" : "Suryanshu Negi",
        "class":"python",
        "marks" : 90,
    },
    "student_2" :{
        "name" : "Shubham",
        "class":"python",
        "marks" : 70,
    },
    'student_3' : {
        "name" : "Aman",
        "class" : "python",
        "marks" : 40,
    },
    'student_4 ': {
        "name" : "Rani",
        "class" : "javascript",
        "marks" : 50,
    }
}
student_input = input("Enter a student's name: ")

found = False

for student in student_dict.values():
    if student["name"].lower() == student_input.lower():
        print(f"{student_input}'s marks: {student['marks']}")
        found = True
        break

if not found:
    print("Student not found.")
