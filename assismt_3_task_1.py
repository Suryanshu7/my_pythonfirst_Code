"""
Functions & Modules in Python
Task 1: Calculate Factorial Using a Function
Problem Statement: Write a Python program that:
    1.   Defines a function named factorial that takes a number as an
            argument and calculates its factorial using a loop or recursion.
    2.   Returns the calculated factorial.
    3.   Calls the function with a sample number and prints the output.

"""

def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return "Factorial is not defined for negative numbers"
    else:
        return num * factorial(num - 1)
    #return factorial(num)
fact = int(input("Enter a number: "))
if fact < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"factorial of {fact} is : {factorial(fact)}")


# with loop
def factorial_2(number):
    result = 1
    for i in range(1,number + 1):
        result *= i
    return result
fact_2 = int(input("Enter a number: "))
if fact_2 < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"factorial using loop of {fact_2} is : {factorial_2(fact_2)}")


# with recursion
def factorial_3(num):
    if num == 0 or num == 1:   # Base case
        return 1
    else:
        return num * factorial_3(num - 1)
fact_3 = int(input("Enter a number: "))
if fact_3 < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"factorial using recursion of {fact_3} is : {factorial_3(fact_3)}")