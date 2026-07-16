"""
   Task 1: Check if a Number is Even or Odd
    Problem Statement: Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
                                       """
user_input = int(input("Enter a number:\t"))
if user_input % 2 == 0:
      print(f"{user_input} is an even number")
else:
    print(f"{user_input} is an odd number")