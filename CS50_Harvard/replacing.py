#Sometimes we might want to replace texts/ or certain alphabest in a sentence.
#For example: we have a sentence 

#Cat gave birth to chicken.
#we want to replace chicken to kittens while printing it.
#note it is case-sensitive so make sure the old one is  written the same it is in the variable stored.

#to do that we use replace function.

name = "Cat gave birth to chicken"
print(name.replace("chicken","kittens"))
print(name.replace("Chicken","kit"))
#Here in LOC 12 i have used C for Chicken .... this will not function.