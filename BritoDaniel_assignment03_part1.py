#Daniel Brito
#db4471
#Assignment 3 Part 1, Prof. Khye
import random
ran_num=random.randint(1, 3)
game_type=input("What type of problem do you want to try?  ADDITION, SUBTRACTION, MULTIPLICATION or RANDOM? ")

if game_type=="ADDITION":
    print("Selection saved - ADDITION")
    print("Operator to use: +")
    
elif game_type=="Subtraction":
    print("Selection saved - SUBTRACTION")
    print("Operator to use: -")
    
elif game_type=="Subtraction":
    print("Selection saved - MULTIPLICATION")
    print("Operator to use: *")

elif game_type=="RANDOM":
    ran_num=random.randint(1, 3)
    if ran_num==1:
            print("... we selected Addition as your random problem type")
            print("Operator to use: + ")
            
    if ran_num==2:
            print("... we selected Subtraction as your random problem type")
            print("Operator to use: - ")
            
    if ran_num==3:
            print("... we selected Multiplication as your random problem type")
            print("Operator to use: * ")

else:
    print("Invalid choice, game will end now.")

#Variables
random_number_for_math1=random.randint(1, 10)
random_number_for_math2=random.randint(1, 10)
add_answer=random_number_for_math1 + random_number_for_math2
sub_answer=random_number_for_math1 - random_number_for_math2
mult_answer=random_number_for_math1 * random_number_for_math2
sub_answer2=random_number_for_math1 - random_number_for_math2
add_answer2=random_number_for_math1 + random_number_for_math2
mult_answer2=random_number_for_math1 * random_number_for_math2
ranadd_answer=random_number_for_math1+random_number_for_math2
ranadd_answer2=random_number_for_math1+random_number_for_math2
ransub_answer=random_number_for_math1-random_number_for_math2
ransub_answer2=random_number_for_math1-random_number_for_math2
ranmult_answer=random_number_for_math1*random_number_for_math2
ranmult_answer2=random_number_for_math1*random_number_for_math2
sub_answer3=random_number_for_math1 - random_number_for_math2
add_answer3=random_number_for_math1 + random_number_for_math2
mult_answer3=random_number_for_math1 * random_number_for_math2
ranadd_answer3=random_number_for_math1+random_number_for_math2
ransub_answer3=random_number_for_math1-random_number_for_math2
ranmult_answer3=random_number_for_math1*random_number_for_math2

#addition option
if game_type=="ADDITION":
    #1st try
    print("Guess #1")
    print("What is", random_number_for_math1, "+", random_number_for_math2,"?")
    add_answer=random_number_for_math1 + random_number_for_math2
    user_answer_add=int(input("What is your answer? "))

    if add_answer==user_answer_add:
        print("You answered correctly!")

    else:
        #incorrect 1st try; only two scenarios: > correct answer, or < correct answer
        print("You did not answer correctly on your first try.")#correct 1st try

        if add_answer>user_answer_add: 
            print("Your answer was too low. Try a higher number next time.")
        else:
            print("Your answer was too high. Try a lower number next time.")
        
        print()
        #2nd try
        print("Guess #2")
        print("What is", random_number_for_math1, "+", random_number_for_math2,"?")
        user_answer_add2=int(input("What is your answer? "))

        if add_answer==user_answer_add2:
            print("You answered correctly!")#correct 2nd try

        else:
            #incorrect 2nd try
            print("You did not answer correctly on your second try.")
                
            if add_answer>user_answer_add2:
                print("Your answer was too low. Try a higher number next time.")
            else:
                print("Your answer was too high. Try a lower number next time.")

            print()
            #3rd try
            print("Guess #3")
            print("What is", random_number_for_math1, "+", random_number_for_math2,"?")
            user_answer_add3=int(input("What is your answer? "))

            if add_answer==user_answer_add3: 
                print("You answered correctly!")

            else:
                #incorrect 3rd try
                print("You did not answer correctly on your third try. The correct answer was",add_answer)

#subtraction option
if game_type=="SUBTRACTION":
    #1st try
    print("Guess #1")
    print("What is", random_number_for_math1, "-", random_number_for_math2,"?")
    sub_answer=random_number_for_math1 - random_number_for_math2
    user_answer_sub=int(input("What is your answer? "))

    if sub_answer==user_answer_sub:
        print("You answered correctly!")

    else:
        #incorrect 1st try; only two scenarios: > correct answer, or < correct answer
        print("You did not answer correctly on your first try.")#correct 1st try

        if sub_answer>user_answer_sub: 
            print("Your answer was too low. Try a higher number next time.")
        else:
            print("Your answer was too high. Try a lower number next time.")
        
        print()
        #2nd try
        print("Guess #2")
        print("What is", random_number_for_math1, "-", random_number_for_math2,"?")
        user_answer_sub2=int(input("What is your answer? "))

        if sub_answer==user_answer_sub2:
            print("You answered correctly!")#correct 2nd try

        else:
            #incorrect 2nd try
            print("You did not answer correctly on your second try.")
                
            if sub_answer>user_answer_sub2:
                print("Your answer was too low. Try a higher number next time.")
            else:
                print("Your answer was too high. Try a lower number next time.")

            print()
            #3rd try
            print("Guess #3")
            print("What is", random_number_for_math1, "", random_number_for_math2,"?")
            user_answer_sub3=int(input("What is your answer? "))

            if sub_answer==user_answer_sub3: 
                print("You answered correctly!")

            else:
                #incorrect 3rd try
                print("You did not answer correctly on your third try. The correct answer was",sub_answer)#subtraction option

#multiplication option
if game_type=="MULTIPLICATION":
    #1st try
    print("Guess #1")
    print("What is", random_number_for_math1, "*", random_number_for_math2,"?")
    mult_answer=random_number_for_math1 * random_number_for_math2
    user_answer_mult=int(input("What is your answer? "))

    if mult_answer==user_answer_mult:
        print("You answered correctly!")

    else:
        #incorrect 1st try; only two scenarios: > correct answer, or < correct answer
        print("You did not answer correctly on your first try.")#correct 1st try

        if mult_answer>user_answer_mult: 
            print("Your answer was too low. Try a higher number next time.")
        else:
            print("Your answer was too high. Try a lower number next time.")
        
        print()
        #2nd try
        print("Guess #2")
        print("What is", random_number_for_math1, "*", random_number_for_math2,"?")
        user_answer_mult2=int(input("What is your answer? "))

        if mult_answer==user_answer_mult2:
            print("You answered correctly!")#correct 2nd try

        else:
            #incorrect 2nd try
            print("You did not answer correctly on your second try.")
                
            if mult_answer>user_answer_mult2:
                print("Your answer was too low. Try a higher number next time.")
            else:
                print("Your answer was too high. Try a lower number next time.")

            print()
            #3rd try
            print("Guess #3")
            print("What is", random_number_for_math1, "*", random_number_for_math2,"?")
            user_answer_mult3=int(input("What is your answer? "))

            if mult_answer==user_answer_mult3: 
                print("You answered correctly!")

            else:
                #incorrect 3rd try
                print("You did not answer correctly on your third try. The correct answer was",mult_answer)#multiplication option

#random addition option
if ran_num==1:
    #1st try
    print("Guess #1")
    print("What is", random_number_for_math1, "+", random_number_for_math2,"?")
    ranadd_answer=random_number_for_math1 + random_number_for_math2
    user_answer_ranadd=int(input("What is your answer? "))

    if ranadd_answer==user_answer_ranadd:
        print("You answered correctly!")

    else:
        #incorrect 1st try; only two scenarios: > correct answer, or < correct answer
        print("You did not answer correctly on your first try.")#correct 1st try

        if ranadd_answer>user_answer_ranadd: 
            print("Your answer was too low. Try a higher number next time.")
        else:
            print("Your answer was too high. Try a lower number next time.")
        
        print()
        #2nd try
        print("Guess #2")
        print("What is", random_number_for_math1, "+", random_number_for_math2,"?")
        user_answer_ranadd2=int(input("What is your answer? "))

        if ranadd_answer==user_answer_ranadd2:
            print("You answered correctly!")#correct 2nd try

        else:
            #incorrect 2nd try
            print("You did not answer correctly on your second try.")
                
            if ranadd_answer>user_answer_ranadd2:
                print("Your answer was too low. Try a higher number next time.")
            else:
                print("Your answer was too high. Try a lower number next time.")

            print()
            #3rd try
            print("Guess #3")
            print("What is", random_number_for_math1, "+", random_number_for_math2,"?")
            user_answer_ranadd3=int(input("What is your answer? "))

            if ranadd_answer==user_answer_ranadd3: 
                print("You answered correctly!")

            else:
                #incorrect 3rd try
                print("You did not answer correctly on your third try. The correct answer was",ranadd_answer)#random addition option              

#random subtraction option
if ran_num==2:
    #1st try
    print("Guess #1")
    print("What is", random_number_for_math1, "-", random_number_for_math2,"?")
    ransub_answer=random_number_for_math1 - random_number_for_math2
    user_answer_ransub=int(input("What is your answer? "))

    if ransub_answer==user_answer_ransub:
        print("You answered correctly!")

    else:
        #incorrect 1st try; only two scenarios: > correct answer, or < correct answer
        print("You did not answer correctly on your first try.")#correct 1st try

        if ransub_answer>user_answer_ransub: 
            print("Your answer was too low. Try a higher number next time.")
        else:
            print("Your answer was too high. Try a lower number next time.")
        
        print()
        #2nd try
        print("Guess #2")
        print("What is", random_number_for_math1, "-", random_number_for_math2,"?")
        user_answer_ransub2=int(input("What is your answer? "))

        if ransub_answer==user_answer_ransub2:
            print("You answered correctly!")#correct 2nd try

        else:
            #incorrect 2nd try
            print("You did not answer correctly on your second try.")
                
            if ransub_answer>user_answer_ransub2:
                print("Your answer was too low. Try a higher number next time.")
            else:
                print("Your answer was too high. Try a lower number next time.")

            print()
            #3rd try
            print("Guess #3")
            print("What is", random_number_for_math1, "-", random_number_for_math2,"?")
            user_answer_ransub3=int(input("What is your answer? "))

            if ransub_answer==user_answer_ransub3: 
                print("You answered correctly!")

            else:
                #incorrect 3rd try
                print("You did not answer correctly on your third try. The correct answer was",ransub_answer)#random subtraction option

#random multiplication option
if ran_num==3:
    #1st try
    print("Guess #1")
    print("What is", random_number_for_math1, "*", random_number_for_math2,"?")
    ransub_answer=random_number_for_math1 * random_number_for_math2
    user_answer_ranmult=int(input("What is your answer? "))

    if ranmult_answer==user_answer_ranmult:
        print("You answered correctly!")

    else:
        #incorrect 1st try; only two scenarios: > correct answer, or < correct answer
        print("You did not answer correctly on your first try.")#correct 1st try

        if ranmult_answer>user_answer_ranmult: 
            print("Your answer was too low. Try a higher number next time.")
        else:
            print("Your answer was too high. Try a lower number next time.")
        
        print()
        #2nd try
        print("Guess #2")
        print("What is", random_number_for_math1, "*", random_number_for_math2,"?")
        user_answer_ranmult2=int(input("What is your answer? "))

        if ranmult_answer==user_answer_ranmult2:
            print("You answered correctly!")#correct 2nd try

        else:
            #incorrect 2nd try
            print("You did not answer correctly on your second try.")
                
            if ranmult_answer>user_answer_ranmult2:
                print("Your answer was too low. Try a higher number next time.")
            else:
                print("Your answer was too high. Try a lower number next time.")

            print()
            #3rd try
            print("Guess #3")
            print("What is", random_number_for_math1, "*", random_number_for_math2,"?")
            user_answer_ranmult3=int(input("What is your answer? "))

            if ranmult_answer==user_answer_ranmult3: 
                print("You answered correctly!")

            else:
                #incorrect 3rd try
                print("You did not answer correctly on your third try. The correct answer was",ranmult_answer)#random multiplication option

