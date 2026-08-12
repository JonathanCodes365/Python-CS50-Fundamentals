# Problem: Combine Two Lists
# You are given:
# a = [1, 2, 3]
# b = [4, 5]
# Extend a using b.
# Then extend a again using:
# c = [6, 7, 8]
# Expected output:
# [1, 2, 3, 4, 5, 6, 7, 8]
# Requirements:
# - Use extend().
# - Do not create a new list.

a= [1,2,3]
b=[4,5]
c = [6,7,8]
a.extend(b)
a.extend(c)
print(a)