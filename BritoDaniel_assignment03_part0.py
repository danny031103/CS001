#Rectangle Simulator
#Daniel Brito
#db4471

#Ask for user input
width_1=int(input("Enter the width for Rectangle #1: "))
length_1=int(input("Enter the length for Rectangle #1: "))
width_2=int(input("Enter the width for Rectangle #2: "))
length_2=int(input("Enter the length for Rectangle #2: "))

#Perform Calculations
area_1=width_1*length_1
area_2=width_2*length_2

print() 

print("Rectangle #1 has an area of",area_1)
print("Rectangle #2 has an area of",area_2)

#Check if they are squares
if width_1==length_1:
    print("Rectangle #1 is a square!")

if width_2==length_2:
    print("Rectangle #2 is a square!")

print()

#Determine which rectangle has a larger area, or if they are equal
if area_1>area_2:
    print("Rectangle #1 is larger than Rectangle #2")

elif area_2>area_1:
    print("Rectangle #2 is larger than Rectangle #1")

elif area_1==area_2:
    print("Rectangle #1 and Rectangle #2 are the same size")
