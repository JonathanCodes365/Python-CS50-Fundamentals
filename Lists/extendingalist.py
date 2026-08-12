#we are doing this after using the append method.

#So , using the append method what we obtained was the ability to add/append new 
#variables , expressions, another list.

#But the thing was when adding another list we are obtaining it in the form of a seperate
#list as 1 element itself.

#example:
name = ["A", "B","C",["D", "E"]]

#But what if i want something like name = [A,B,C,D,E,.....]
#We obtain this using the extend method.

name1 = ["A","B","C"]
name1.extend(["D","E"])
print(name1)

#now the next question you might be having: at least what i am having rn is :
name = ["A", "B","C",["D", "E"]]
#can we change the ["D", "E" ] itself to D ,E ?
#turns out we cant just use the extend function to do this.
#if we used the extend function in this...

name.extend(name[3])#Considering the list D,E is in index 3

print(name)
#['A', 'B', 'C', ['D', 'E'], 'D', 'E'] we get this as our result
#So, we need a different operation to this ....
#We will use list slicing for this but this will come in the later aspect of the program.


#Next up is using insert() method in a list.