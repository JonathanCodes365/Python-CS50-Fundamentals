# Problem: Build the Correct List
# You are given:
# numbers = [20, 50]
# Your task is to use insert() to transform the list into:
# [10, 20, 30, 40, 50, 60]
# Rules:
# - You may only use insert().
# - Do not create a new list.
# - You must add 10, 30, 40, and 60.
# Write your solution below.

numbers = [20, 50]
numbers.insert(0,10)
numbers.insert(2,30)
numbers.insert(3,40)
numbers.insert(5,60)
print(numbers)
