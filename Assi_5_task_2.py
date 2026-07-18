# Task 2: Demonstrate List Slicing
"""
        Problem Statement: Write a Python program that:
    1.Creates a list of numbers from 1 to 10.
    2.Extracts the first five elements from the list.
    3.Reverses these extracted elements.
    4.Prints both the extracted list and the reversed list
"""


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = list_1
data_1= (list_1[:5])
data_2 = (list_1[:5][::-1])
print(f"Original list: {data}")
print(f"Extracted list: {data_1}")
print(f"Reversed list: {data_2}")
