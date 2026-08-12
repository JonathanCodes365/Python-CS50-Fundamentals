#It is the opposite of Replace.
#It joins 2 different strings/lists into 1.

#Example:

parts = ["My", "Name","Is","Ngawang","Sherpa"]
#Since, this is a list : we can access it using indexing.
print(parts[0])

name = " ".join(parts)
#this is our default setting " ".join(parts)... 
#Notice how there is a " " .i.e. whitespace which means connect these lists using a whitespace.
print(name)

#we can change that default setting as well.
xyz = "-".join(parts)
print(xyz)