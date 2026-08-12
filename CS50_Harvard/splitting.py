text = "apple ,banana, orange"

#This is default and it states split whenever you find a whitespace.
parts = text.split()

#note the parts after the split are list.
print(parts)
#so we can access particular part only as well.
print(parts[0])
print(parts[1])

parts = text.split(",")
#it means split whenever you find ,
#Hence in apple,banana,orange
#Split must occur after , .i.e. result must be apple banana and orange seperated as diff. lists.

print(parts)