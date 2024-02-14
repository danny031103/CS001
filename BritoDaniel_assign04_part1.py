#Daniel Brito
#Prof. Khye
#Dice Roll Game

import random

dice=int(input("How many sides should the dice have? (even integers only)"  ))

while dice%2!=0:
    print("Invalid Selection")
    dice=int(input("How many sides should the dice have? (even integers only)"  ))


rollagain="yes"

#Variables
rollnum=1
high=0
highlow=0
even=0
odd=0
mixed=0
sumroll=0
neighbor=0
double=0
middle=0
snakeeyes=0
side1_sum=0
side2_sum=0
div=0

#Large While statement to keep the game running, followed by if statements to record data
while rollagain=="yes":
    print("Rolling the dice...")

    side1=random.randint(1,dice)
    side2=random.randint(1,dice)
    side1_sum+=side1
    side2_sum+=side2
    
    if side1==side2 and (side1+side2!=2):
        print(str(rollnum)+".", "die roll is", "*"+str(side1)+"*", "*"+str(side2)+"*", "Double!")
        rollnum+=1
        double+=1
        div+=1
        print()

    elif side1+side2==2:
        print(str(rollnum)+".", "die roll is", "*"+str(side1)+"*", "*"+str(side2)+"*", "Odd! Double! Snake Eyes!")
        double+=1
        snakeeyes+=1
        odd+=1
        div+=3
        rollagain="no"
        print()

    elif side1+side2==dice+1:
        print(str(rollnum)+".", "die roll is", "*"+str(side1)+"*", "*"+str(side2)+"*", "Middle!")
        rollnum+=1
        middle+=1
        div+=1
        print()
        
    elif (side1-side2==1) or (side2-side1==1):
        print(str(rollnum)+".", "die roll is", "*"+str(side1)+"*", "*"+str(side2)+"*",  "Mixed! Neighbor!")
        rollnum+=1
        neighbor+=1
        mixed+=1
        div+=2
        print()

    elif (dice==(side1+side2)):
        print(str(rollnum)+".", "die roll is", "*"+str(side1)+"*", "*"+str(side2)+"*", "Sum Value!")
        rollnum+=1
        sumroll+=1
        div+=1
        print()

    elif (side1%2==0 and side2%2!=0) or (side1%2!=0 and side2%2==0):
        print(str(rollnum)+".", "die roll is", "*"+str(side1)+"*", "*"+str(side2)+"*", "Mixed!")
        rollnum+=1
        mixed+=1
        div+=1
        print()

    elif side1%2!=0 and side2%2!=0:
        print(str(rollnum)+".", "die roll is", "*"+str(side1)+"*", "*"+str(side2)+"*", "Odd!")
        rollnum+=1
        odd+=1
        div+=1
        print()

    elif side1%2==0 and side2%2==0:
        print(str(rollnum)+".", "die roll is", "*"+str(side1)+"*", "*"+str(side2)+"*", "Even!")
        rollnum+=1
        even+=1
        div+=1
        print()

    elif (side1==dice and side2==1) or (side1==1 and side2==dice):
        print(str(rollnum)+".", "die roll is", "*"+str(side1)+"*", "*"+str(side2)+"*", "High/low! Mixed!")
        rollnum+=1
        highlow+=1
        mixed+=1
        div+=2
        print()

    if side1==dice and side2==dice:
        print(str(rollnum)+".", "die roll is", side1, side2, "High!")
        rollnum+=1
        high+=1
        div+=1
        print()

    else:
        print()


totalrolls=high+highlow+even+odd+mixed+sumroll+neighbor+middle+double+snakeeyes
if highlow-mixed<0:
    phighlow=0
elif odd-double-snakeeyes<0:
    podd=0
elif mixed-highlow<0:
    pmixed==0
elif neighbor-mixed<0:
    pneighbor=0
elif double-snakeeyes-odd<0:
    pdouble=0

avgside1_sum=format((side1_sum/rollnum), ",.2f")
avgside2_sum=format((side2_sum/rollnum), ",.2f")

#formatting 1
phigh= format((high/div)*100, ",.2f")
phighlow=format((highlow/div)*100, ",.2f")
peven=format((even/div)*100, ",.2f")
podd=format((odd/div)*100, ",.2f")
pmixed=format((mixed/div)*100, ",.2f")
psumroll=format((sumroll/div)*100, ",.2f")
pneighbor=format((neighbor/div)*100, ",.2f")
pmiddle=format((middle/div)*100, ",.2f")
pdouble=format(((double)/div)*100, ",.2f")
psnakeeyes=format((snakeeyes/div)*100, ",.2f")
    
#printing results
print("You finally got snake eyes on roll number:", rollnum)
print("Along the way you rolled HIGH", high, "time(s).", "(",phigh,"% of all rolls)")
print("Along the way you rolled HIGH/LOW", highlow, "time(s).", "(",phighlow,"% of all rolls)")
print("Along the way you rolled EVEN", even, "time(s).", "(",peven,"% of all rolls)")
print("Along the way you rolled ODD", odd, "time(s).", "(",podd,"% of all rolls)")
print("Along the way you rolled MIXED", mixed, "time(s).", "(",pmixed,"% of all rolls)")
print("Along the way you rolled SUM VALUE", sumroll, "time(s).", "(",psumroll,"% of all rolls)")
print("Along the way you rolled NEIGHBOR", neighbor, "time(s).", "(",pneighbor,"% of all rolls)")
print("Along the way you rolled MIDDLE", middle, "time(s).", "(",pmiddle,"% of all rolls)")
print("Along the way you rolled DOUBLE", double-1, "time(s).", "(",pdouble,"% of all rolls)")
print("Along the way you rolled SNAKEEYES", snakeeyes, "time(s).", "(",psnakeeyes,"% of all rolls)")
print("Average roll for die #1", avgside1_sum)
print("Average roll for die #2", avgside2_sum)






























