"""
Write and Append Data to a File

Problem Statement: Write a Python program that:
    1.Takes user input and writes it to a file named output.txt.
    2.Appends additional data to the same file.
    3.Reads and displays the final content of the file.
"""
# Step 1: Take input and write to file
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("\nData successfully written to output.txt.\n")

# Step 2: Take more input and append
more_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(more_text + "\n")

print("\nData successfully appended.\n")

# Step 3: Read and display final content
print("Final content of output.txt:\n")

with open("output.txt", "r") as file:
    print(file.read(), end="")