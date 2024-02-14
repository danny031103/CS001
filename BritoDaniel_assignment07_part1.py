#Daniel Brito
#db4471
#Assignment 7 Part 1
#Prof. Khye
################################################################################################################################################
#USERNAME VALIDATOR

criteria=0
while criteria<6:
    username=input("Enter Username: ")
    uppercasecount=0
    lowercasecount=0
    digitcount=0
    stringusername=str(username)

    print("* Length of username: ", len(stringusername))

    if len(stringusername)<8 and len(stringusername)>15:
        print("ERROR - username must be 8 to 15 characters long")
        
    if stringusername.isalnum()== True:
        print("* All characters are alphabetic or numeric: True")
        criteria+=1
    else:
        print("* All characters are alphabetic or numeric: False")
        print("ERROR - username cannot contain non-alphabetic or non-numeric characters")

    if username[0].isdigit() == True:
        print("* First character is a digit: True")
        print("ERROR - first character cannot be a digit")

    else:
        print("* First character is a digit: False")
        criteria+=1
        
    if username[-1].isdigit() == True:
        print("* Last character is a digit: True")
        print("ERROR - last character cannot be a digit")

    else:
        print("* Last character is a digit: False")
        criteria+=1
        
    for x in username:
        if(x.isupper()):
            
            uppercasecount= uppercasecount + 1
            
    if uppercasecount > 0:
        
        if uppercasecount > 8:
            print("# of uppercase letters:", uppercasecount)
            criteria += 1
        else:
            print("# of uppercase letters:", uppercasecount)
            criteria += 1
    else:
        print("ERROR - username must contain at least one uppercase character")

    for x in username:
        if(x.islower()):
            
            lowercasecount= lowercasecount + 1
            
    if lowercasecount > 0:
        
        if lowercasecount > 8:
            print("# of lowercase letters:", lowercasecount)
            criteria += 1
        else:
            print("# of lowercase letters:", lowercasecount)
            criteria += 1
    else:
        print("ERROR - username must contain at least one lowercase character")

    for x in username:
        if(x.isdigit()):
            
            digitcount= digitcount + 1
            
    if digitcount > 0:
        
        if digitcount > 8:
            print("# of numbers letters:", digitcount)
            criteria += 1
        else:
            print("# of numbers letters:", digitcount)
            criteria += 1
    else:
        print("ERROR - username must contain at least one digit")

if criteria==6:
    print("Valid Username")
    
else:
    print("Invalid Password, try again.")
print()
        

###################################################################################################################################################################
#PASSWORD VALIDATOR

pcriteria=0
while pcriteria<6:
    password=input("Enter a password: ")
    puppercasecount=0
    plowercasecount=0
    pdigitcount=0
    pstringpassword=str(password)

    print("* Length of password: ", len(pstringpassword))

    if len(pstringpassword)<8:
        print("ERROR - username must be at least 8 characters long")

    else:
        pcriteria+=1

    if username in password==True:
        print("ERROR - username cannot exist within password")

    else:
        print("* Username is part of password: False")
        pcriteria+=1
        
    for x in password:
        if(x.isupper()):
            puppercasecount= puppercasecount + 1
            
    if puppercasecount > 0:
        
        if puppercasecount > 8:
            print("* # of uppercase letters:", puppercasecount)
            pcriteria += 1
        else:
            print("* # of uppercase letters:", puppercasecount)
            pcriteria += 1
    else:
        print("ERROR - username must contain at least one uppercase character")

    for x in password:
        if(x.islower()):
            plowercasecount= plowercasecount + 1
            
    if plowercasecount > 0:
        
        if plowercasecount > 8:
            print("* # of lowercase letters:", plowercasecount)
            pcriteria += 1
        else:
            print("* # of lowercase letters:", plowercasecount)
            pcriteria += 1
    else:
        print("ERROR - password must contain at least one lowercase character")

    for x in password:
        if(x.isdigit()):
            pdigitcount= pdigitcount + 1
            
    if pdigitcount > 0:
        
        if pdigitcount > 8:
            print("* # of numbers letters:", pdigitcount)
            pcriteria += 1
        else:
            print("* # of numbers letters:", pdigitcount)
            pcriteria += 1
    else:
        print("ERROR - password must contain at least one digit")

    if password.isalnum()== True:
        print("* # of special characters in the password: 0")
        print("ERROR - password must contain at least one special character")

    else:
        nonabcchars=len(password)-pdigitcount-plowercasecount-puppercasecount
        print("* # of special characters in the password: ",nonabcchars)

    upper = 0
    lower = 0
    digit = 0
    special = 0
    invalid = 0

    for character in password:
        if character.isupper():
            upper += 1
        elif character.islower():
            lower += 1
        elif character.isdigit():
            digit += 1
        elif character in "#$%!":
            special += 1
        else:
            invalid += 1

    print("# of special characters:", special)
    print("# of invalid characters:", invalid)

    if invalid>0:
        print("ERROR - password cannot contain invalid character")

    else:
        pcriteria+=1
        

    if pcriteria==6:
        print("Password is Valid!")

    else:
        print("Password is not valid, try again.")




            
    
    
    
