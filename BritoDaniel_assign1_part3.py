#Daniel Brito, September 11, 2022, Prof. Khye
#Program to present names in all possible combinations
#Prompt users for their names
name1=input("Please enter name #1: ")
name2=input("Please enter name #2: ")
name3=input("Please enter name #3: ")
print()
#Introduce the program function
print("Here are your names in every possible order:")
dashedline="Here are your names in every possible order:"
print("-"*len(dashedline))
print()
#First sequence
print("1.",name1+",", name2+",", name3)
print()
#Second Sequence
print("2.","**"+name1+"**","**"+name3+"**","**"+name2+"**")
print()
#Third Sequence
print("3.", name2+"-"+name1+"-"+name3)
print()
#Fourth Sequence
print("4.",name2)
print(name3)
print(name1)
print()
#Fifth Sequence
print("5.",name3)
print("   "+name2+"!")
print("   "+name1)
print()
#Sixth Sequence
print("6.","---"+name3)
print("   ------"+name1)
print("   ---------"+name2)
