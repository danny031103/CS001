#Daniel Brito
#db4471
#Prof. Khye
#Worked with Salam Haroun 
#Assignment 5 Part 1

#Amount of Students
student_total=int(input("How many students are in your class? "))

#Validate student amount
while student_total<1:
    print ("Invalid number of students; please try again.")
    student_total=int(input("How many students are in your class? "))
    print()

test_total=int(input("How many tests in this class? "))

while test_total<0:
    print("Invalid number of tests; please try again.")
    test_total= int(input ("How many tests in this class? "))


#Extra Credit
extra_credit=(input("Is extra credit allowed in your class? (1-yes/2-no)"))

#Validate extra credit
while (extra_credit!='yes') and (extra_credit!='no'):
    print ("Invalid, please try again.")
    extra_credit=(input("Is extra credit allowed in your class? (yes/no)"))
    print()

#Drop Lowest Grade
lowest_grade=(input("Does the lowest grade get dropped? (yes/no) "))

#Validate lowest grade
while (lowest_grade!="yes") and (lowest_grade!="no"):
    print ("Invalid, please try again.")
    lowest_grade=(input("Does the lowest grade get dropped? (yes/no) "))
    print()

#User Display of Text   
print()
print("Thanks, here we go!")
print()

#Variables
studentpoints1=0
class_averages=0

#Extra Credit Not Allowed, no dropping score
if extra_credit=="no" and lowest_grade=="no":
    for student in range(0,student_total):
        print()
        print("*** Student #"+str(student+1)+" ***")
        studentpoints=0
        class_averages=0
        student_lettergrade=" "
        a_average=0
        b_average=0
        c_average=0
        d_average=0
        f_average=0

        for test in range(0,test_total):

            score=float(input("Enter a score for test #"+str(test+1)+":"))

            while score<0 and score>100:
                print("Invalid Score, try again.")
                score=float(input("Enter a score for test #"+str(test+1)+":"))

            studentpoints+=score
            studentpoints1+=score
            average_student=(studentpoints/test_total)

            if average_student>=90:
                student_lettergrade="A"
                
            elif average_student>=80 and average_student<90:
                student_lettergrade="B"

            elif average_student>=70 and average_student<80:
                student_lettergrade="C"
                
            elif average_student>=60 and average_student<70:
                student_lettergrade="D"
                
            else:
                student_lettergrade=="F"

        print("Average score for student"+str(student+1)+": ", average_student, "("+student_lettergrade+")")
        print()

    if average_student>=90:
        a_average+=1

    elif average_student>=80 and average_student<90:
        b_average+=1

    elif average_student>=70 and average_student<80:
        c_average+=1

    elif average_student>=60 and average_student<70:
        d_average+=1

    else:
        f_average+=1


#Extra Credit allowed, no dropping Score
elif extra_credit=="yes" and lowest_grade=="no":
    for student in range(0,student_total):
        print()
        print("*** Student #"+str(student+1)+" ***")
        studentpoints=0
        class_averages=0
        student_lettergrade=" "
        a_average=0
        b_average=0
        c_average=0
        d_average=0
        f_average=0

        for test in range(0,test_total):

            score=float(input("Enter a score for test #"+str(test+1)+":"))

            while score<0:
                print("Invalid Score, try again.")
                score=float(input("Enter a score for test #"+str(test+1)+":"))

            studentpoints+=score
            studentpoints1+=score
            average_student=(studentpoints/test_total)

            if average_student>=90:
                student_lettergrade="A"
                
            elif average_student>=80 and average_student<90:
                student_lettergrade="B"

            elif average_student>=70 and average_student<80:
                student_lettergrade="C"
                
            elif average_student>=60 and average_student<70:
                student_lettergrade="D"
                
            else:
                student_lettergrade="F"

        print("Average score for student #"+str(student+1)+": ", average_student, "("+student_lettergrade+")")
        print()
        
    if average_student>=90:
        a_average+=1

    elif average_student>=80 and average_student<90:
        b_average+=1

    elif average_student>=70 and average_student<80:
        c_average+=1

    elif average_student>=60 and average_student<70:
        d_average+=1

    else:
        f_average+=1
        
#Extra Credit not allowed, dropping score allowed
elif extra_credit=="no" and lowest_grade=="yes":
    for student in range(0,student_total):
        print()
        print("*** Student #"+str(student+1)+" ***")
        studentpoints=0
        class_averages=0
        student_lettergrade=" "
        a_average=0
        b_average=0
        c_average=0
        d_average=0
        f_average=0

        for test in range(0,test_total):

            score=float(input("Enter a score for test #"+str(test+1)+":"))

            while score<0 and score>100:
                print("Invalid Score, try again.")
                score=float(input("Enter a score for test #"+str(test+1)+":"))

            if test==0:
                smallest_num=score
                
            else:

                if score<smallest_num: 
                    smallest_num=score

            studentpoints+=score
            studentpoints1+=score
            average_studentd=((studentpoints-smallest_num)/(test_total-1))

            if average_studentd>=90:
                student_lettergrade="A"
                
            elif average_studentd>=80 and average_studentd<90:
                student_lettergrade="B"

            elif average_studentd>=70 and average_studentd<80:
                student_lettergrade="C"
                
            elif average_studentd>=60 and average_studentd<70:
                student_lettergrade="D"
                
            else:
                student_lettergrade="F"

        print("Average score for student #"+str(student+1)+": ", average_studentd, "("+student_lettergrade+")")
        print()
        
    if average_studentd>=90:
        a_average+=1

    elif average_studentd>=80 and average_studentd<90:
        b_average+=1

    elif average_studentd>=70 and average_studentd<80:
        c_average+=1

    elif average_studentd>=60 and average_studentd<70:
        d_average+=1

    else:
        f_average+=1

#Extra Credit allowed, dropping score allowed
elif extra_credit=="yes" and lowest_grade=="yes":
    for student in range(0,student_total):
        print()
        print("*** Student #"+str(student+1)+" ***")
        studentpoints=0
        class_averages=0
        student_lettergrade=" "
        a_average=0
        b_average=0
        c_average=0
        d_average=0
        f_average=0

        for test in range(0,test_total):

            score=float(input("Enter a score for test #"+str(test+1)+":"))

            while score<0:
                print("Invalid Score, try again.")
                score=float(input("Enter a score for test #"+str(test+1)+":"))

            if test==0:
                smallest_num=score
                
            else:

                if score<smallest_num: 
                    smallest_num=score
                    
            studentpoints+=score
            studentpoints1+=score
            average_studentd=((studentpoints-smallest_num)/(test_total-1))

            if average_studentd>=90:
                student_lettergrade="A"
                
            elif average_studentd>=80 and average_student<90:
                student_lettergrade="B"

            elif average_studentd>=70 and average_student<80:
                student_lettergrade="C"
                
            elif average_studentd>=63 and average_student<70:
                student_lettergrade="D"
                
            else:
                student_lettergrade="F"

        print("Average score for student #"+str(student+1)+": ", average_studentd, "("+student_lettergrade+")")
        print()

    if average_studentd>=90:
        a_average+=1

    elif average_studentd>=80 and average_studentd<90:
        b_average+=1

    elif average_studentd>=70 and average_studentd<80:
        c_average+=1

    elif average_studentd>=60 and average_studentd<70:
        d_average+=1

    else:
        f_average+=1

overall_avg=0

if lowest_grade=="yes":
    overall_avg=((studentpoints*student_total)-smallest_num)/(test_total-1)*(student_total)

elif lowest_grade=="no":
    overall_avg=((studentpoints1)/(test_total*student_total))

print("Overall Class Average:", overall_avg)
print("# of students who earned an 'A' average:", a_average)
print("# of students who earned an 'B' average:", b_average)
print("# of students who earned an 'C' average:", c_average)
print("# of students who earned an 'D' average:", d_average)
print("# of students who earned an 'F' average:", f_average)
