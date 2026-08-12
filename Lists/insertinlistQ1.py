# Problem: Insert Multiple Elements
# You are given the following list:
# numbers = [10, 20, 40, 50]
# Your task is to:
# 1. Insert 30 between 20 and 40.
# 2. Insert 5 at the beginning of the list.
# 3. Insert 60 at the end of the list.
# Expected output:
# [5, 10, 20, 30, 40, 50, 60]
# Requirements:
# - Use the insert() method for ALL three operations.
# - Do not create a new list.
# Write your solution below:

numbers = [10, 20, 40, 50]
numbers.insert(0,5) 
numbers.insert(3,30)
numbers.insert(6,60)
print(numbers)