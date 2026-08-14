# Problem: Remove Specific Duplicates
# You are given:
# numbers = [10, 20, 30, 20, 40, 20, 50]
# Your task is to remove EVERY occurrence of 20.
# Expected output:
# [10, 30, 40, 50]
# Requirements:
# - Use remove().
# - Do not create a new list.
# - Do not use loops.
# - Do not use sort().
# Write your solution below:

numbers = [10, 20, 30, 20, 40, 20, 50]
numbers.remove(20)
numbers.remove(20)
numbers.remove(20)