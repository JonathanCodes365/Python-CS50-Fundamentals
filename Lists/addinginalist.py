#So , this here is after we did the Changing in a list .

#for example say :

name = ["Michael" , "Sarah" , "Ali" , "Gandhi" , "Churchill"]

#now , if i want to add Teressa on the group .. we simply do:

name.append("Teressa")
print(name)

#Now, the more interesting part is we can even append a list itself within a list.
#Say we have another list called name1

name1 = ["John Doe" ,"Tara Moktan"]
#Now , i want to append this list inside name.

name.append(name1)
print(name)

#It will print :

#['Michael', 'Sarah', 'Ali', 'Gandhi', 'Churchill', 
# 'Teressa', ['John Doe', 'Tara Moktan']]

#Now , what if i want to print John Doe and Tara Moktan?
#It's simple: In python When it is a list inside a list.
#It first acts as a  single element.
#Notice the indexing ... Michael = 0 , sarah =1 , [John Doe, Tara...] = 6

#so if i want to print just the new list
print(name[6])

#if i want to print Tara Moktan
print(name[6][1])


#Finally, i forgot to add :
#we cannot do name = name.append("Rai")

#although name.append("Rai") must add a new str called Rai inside the list called name.
#It returns nothing 

#so when we do name = nothing..
#This doesnt turn out well.
#so if we want to add/append new stuff
#we just do 

#name.append("Rai")