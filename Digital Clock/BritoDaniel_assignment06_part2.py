#Daniel Brito
#db4471
#Prof. Khye
#Math Game with displayed numbers

import digitalclock
import random

print("Addition, Subtraction, and Multiplication Game!")
print()

#User Input for problem number
problems=int(input("How many problems would you like to attempt? "))
while problems<1:
    print("Invalid number, try again")
    problems=int(input("How many problems would you like to attempt? "))

#User input for size of digits printed
digsize=int(input("How wide do you want your digits to be? 5-10: "))
while digsize<5 or digsize>10:
    print("Invalid width, try again.")
    digsize=int(input("How wide do you want your digits to be? 5-10: "))

#User input for character that symbols will be made up of
charchoice=str(input("What character would you like to use? "))
while len(charchoice)>1:
    print("String too long, try again.")
    charchoice=str(input("What character would you like to use? "))

print()
print("Here we go!")
print()

#randnumoperation=1=addition
#randnumoperation=2=subtraction
#Variables
correctcounter=0
x=0
addprobs=0
subprobs=0
addprobsright=0
subprobsright=0
multprobs=0
multprobsright=0

#Number generation,addition
while x<problems:
    randnum1=random.randint(0,9)
    randnum2=random.randint(0,9)
    randnumoperation=random.randint(1,3)
    if randnumoperation==1:
        print()
        print("What is......")
        print(digitalclock.print_number(randnum1,digsize,charchoice))
        print()
        print(digitalclock.plus(digsize,charchoice))
        print()
        print(digitalclock.print_number(randnum2,digsize,charchoice))
        useranswer=int(input("= "))
        print(digitalclock.check_answer(randnum1, randnum2, useranswer,"+"))
        print()
        x+=1
        addprobs+=1
        if useranswer==randnum1+randnum2:
            correctcounter+=1
            addprobsright+=1
            
#Subtraction
    if randnumoperation==2:
        print()
        print("What is......")
        print(digitalclock.print_number(randnum1,digsize,charchoice))
        print()
        print(digitalclock.minus(digsize,charchoice))
        print()
        print(digitalclock.print_number(randnum2,digsize,charchoice))
        useranswer=int(input("= "))
        print(digitalclock.check_answer(randnum1, randnum2, useranswer,"-"))
        print()
        x+=1
        subprobs+=1
        if useranswer==randnum1-randnum2:
            correctcounter+=1
            subprobsright+=1

#Multiplication
    if randnumoperation==3:
        print()
        print("What is......")
        print(digitalclock.print_number(randnum1,digsize,charchoice))
        print()
        print(digitalclock.mult(digsize,charchoice))
        print()
        print(digitalclock.print_number(randnum2,digsize,charchoice))
        useranswer=int(input("= "))
        print(digitalclock.check_answer(randnum1, randnum2, useranswer,"*"))
        print()
        x+=1
        multprobs+=1
        if useranswer==randnum1*randnum2:
            correctcounter+=1
            multprobsright+=1

#Formatting    
if addprobs>0:          
    addpercentage=format((addprobsright/addprobs)*100, ",.2f")
else:
    addpercentage=0

if subprobs>0:
    subpercentage=format((subprobsright/subprobs)*100, ",.2f")
else:
    subpercentage=0

if multprobs>0:
    multpercentage=format((multprobsright/multprobs)*100, ",.2f")
else:
    multpercentage=0

#Displaying Results
print()
print("You got", correctcounter, "out of", problems, "correct!")
print()
print("Total addition problems presented: ", addprobs)
print("Correct addition problems: ", addprobsright, "("+str(addpercentage)+"%)")
print()
print("Total subtraction problems presented: ", subprobs)
print("Correct subtraction problems: ", subprobsright, "("+(str(subpercentage)+"%)"))
print()
print("Total multiplication problems presented: ", multprobs)
print("Correct multiplication problems: ", multprobsright, "("+(str(multpercentage)+"%)"))












































