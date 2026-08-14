# Problem: Find and Remove
# You are given:
# numbers = [10, 20, 30, 40, 50]
# Your task is to:
# 1. Find the index of 40.
# 2. Remove 40 using pop().
# 3. Print the removed value.
# 4. Print the resulting list.
# Expected output:
# 40
# [10, 20, 30, 50]
# Requirements:
# - You must use index().
# - You must use pop().
# - Do not manually use pop(3).
# Write your solution below:

numbers = [10, 20, 30, 40, 50]
x = numbers.index(40)
y = numbers.pop(x)
print(y)
print(numbers)
