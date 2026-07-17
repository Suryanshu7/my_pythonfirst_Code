"""
Module 5: Files, Exceptions, and Errors in Python
Task 1: Read a File and Handle Errors
    Problem Statement:  Write a Python program that:
        1.Opens and reads a text file named sample.txt.
        2.Prints its content line by line.
        3.Handles errors gracefully if the file does not exist.

"""
#  Now let's start the task
with open("sample.txt","wt") as file:
    data = file.write("This is a sample file.\n")
    data1 = file.write("Its contain a multiple lines")

try:
    with open("sample.txt", "r") as file:  #sample1.txt
        for i, line in enumerate(file, start=1):
            print(f"Line {i} : {line.strip()}")
except FileNotFoundError:
    print("the file 'sample.txt' not found")
