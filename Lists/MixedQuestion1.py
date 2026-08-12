# Problem: Fix the List
# You are given a list that contains some elements in the wrong places:
# numbers = [10, 20, 50, 30, 40]
# Your goal is to transform it into:
# [10, 20, 30, 40, 50]
# Rules:
# - You may use insert(), append(), extend(), and list indexing.
# - You may NOT create a new list.
# - You may NOT use sort().
# - You may NOT manually rewrite the entire list.
# Your solution should actually manipulate the existing list.
# Write your solution below:

numbers = [10, 20, 50, 30, 40]
numbers[2]=30
numbers[3]=40
numbers[4]=50
print(numbers)
