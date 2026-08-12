# Problem: Extend a List
# You are given two lists:
# numbers = [10, 20, 30]
# new_numbers = [40, 50, 60]
# Your task is to add all the elements from new_numbers
# to the end of numbers.
# Expected output:
# [10, 20, 30, 40, 50, 60]
# Requirements:
# - Use the extend() method.
# - Do not create a new list.
# Write your solution below:

numbers = [10,20,30]
new_number = [40,50,60]

numbers.extend(new_number)
print(numbers)