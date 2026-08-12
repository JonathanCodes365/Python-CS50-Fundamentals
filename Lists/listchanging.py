#So , one of the key difference between string and lists is this:

#Lists are mutable.
#Meaning: They can be modified.

#Strings cannot be modified.

#Now, you might say ... Hey but we can use the replace() method that we did earlier to 
#modify a string...

name = "Michael Habibi"
#This is one of the misconception that i had regarding strings and variables.
name = name.replace("Habibi", "Jordan")
print(name)

#So what is happening here? Didnt Habibi get modified to Jordan?
#Accurately saying: No!

#So, We must get this straight that:
#Michael Habibi is : different string
#When we say replace Habibi with Jordan... We are creating a string called Michael Jordan
#So, Michael Jordan : different string.

#So, its just that at the beginning name was assigned to Michael Habibi
#and now its assigned to Michael Jordan.
#so we didnot modify the string itself. We just made sure the variable was assigned to
#what we wanted.


#But, this is completely different in lists.

list = ["Chicken", "Orange" , "Apple" , "Mango "]
#Notice : Chicken is a bird in the group of fruits and i want to replace it with guava.
list[0] = "Guava"
print(list)

#So, this is how we change variables inside a lists

#Next ,we will look at how to add things to a list.

