#Daniel Brito
#db4471
#Assignment 7
#Prof. Khye

###########################################################################################################################################################################################
#UP AND DOWN
#65-90 capital letters
#97-122 lowercase

def ascii_shift(word,direction):
    xletter=""
    for x in word:
        if ord(x)==65 and direction=="down":
            letter=90
            xletter+=chr(letter)

        elif ord(x)==90 and direction=="up":
            letter=65
            xletter+=chr(letter)

        elif ord(x)>=65 and ord(x)<=90 and direction=="up":
            letter=ord(x)+1
            xletter+=chr(letter)

        elif ord(x)>=65 and ord(x)<=90 and direction=="down":
            letter=ord(x)-1
            xletter+=chr(letter)
        
        else:
            xletter+=(x)

    return xletter

    if direction!="down" and direction!="up":
        return word
            

print( ascii_shift("apple", "up")) # apple
print(ascii_shift("APPLE", "up")) # BQQMF
print(ascii_shift("APPLE", "down")) # ZOOKD
print(ascii_shift("APPLE 123", "up")) # BQQMF 123
print(ascii_shift("APPLE, PIE, and ZEBRAS", "down")) # ZOOKD, OHD, and YDAQZR
print(ascii_shift("APPLE, PIE, and ZEBRAS", "pikachu")) # APPLE, PIE, and ZEBRAS
print(ascii_shift("", "up")) # (nothing prints, empty string)

#########################################################################################################################################################################################
#SHIFT RIGHT   

def shift_right(string):

    if(len(string)==0):
        return " "

    else:
        return (string[-1] + string[:-1])

print(shift_right("apple")) # eappl
print(shift_right("hello, world!")) # !hello, world
print(shift_right("")) # (nothing prints, empty string)

#########################################################################################################################################################################################

#SHIFT LEFT   

def shift_left(string):

    if(len(string)==0):
        return " "

    else:
        return (string[1:-1]+string[-1]+string[0])

print(shift_left("apple")) # pplea
print(shift_left("hello, world!")) # ello, world!h
print(shift_left("")) # (nothing prints, empty string)
print()
#########################################################################################################################################################################################

#FLIP

def flip(string):
    wordlength=int(len(string))
    wordlengthhalf=int(len(string)/2)
    midpointplusone=wordlengthhalf+1
    word=""
    
    if wordlength%2!=0:
        word+=string[midpointplusone:-1]
        word+=string[-1]
        word+=string[wordlengthhalf]
        word+=string[0:wordlengthhalf]
        return word

    elif wordlength%2==0:
        word+=string[wordlengthhalf:-1]
        word+=string[-1:]
        word+=string[0:wordlengthhalf]
        return word
    
    else:
        word+=""
        return word


print(flip("ABCDEFG")) # EFGDABC
print(flip("123456")) # 456123
print(flip("")) # (nothing prints, empty string)
print()

######################################################################################################################################################################################

#ADD LETTERS
def add_letters(string,number):
    import random
    final=""
    flip=0

    for c in string:
        final+=c
        for i in range(number):
            flip=random.randint(1,2)
            if flip==1:
                x=(random.randint(65,90))
                final+=chr(x)
            else:
                x=(random.randint(97,122))
                final+=chr(x)
    return final   

print(add_letters('Yesok',4))
print()
     
######################################################################################################################################################################################

#DELETE CHARACTERS
def delete_characters(string,number):
    word=""
    x=0
    while x<len(string):
        word = word + string[x]
        x=x+number+1
    return word

word1 = "HdeulHlHom!t"
word2 = "HTLedklFNljioMH!bi"
word3 = "HHHZeZrflqSflzOiosNU!jBk"
word4 = "HFtRKeivFllRNlUlGTaooYwoH!JpXL"

unscrambled1 = delete_characters(word1, 1)
print ("Removing 1 character from", word1, "->", unscrambled1)

unscrambled2 = delete_characters(word2, 2)
print ("Removing 2 characters from", word2, "->", unscrambled2)

unscrambled3 = delete_characters(word3, 3)
print ("Removing 3 characters from", word3, "->", unscrambled3)

unscrambled4 = delete_characters(word4, 4)
print ("Removing 4 characters from", word4, "->", unscrambled4)

print()
######################################################################################################################################################################################

#PART 2B

pattern=input("Enter an encoding pattern, 'end' to end: ")
wordtoencode=input("Enter a word to encode/decode: ")
finalword=""
updatedword=wordtoencode
'''
'A' = add 1 random character after each character (i.e. cat -> cZaZtZ)
'X' = delete 1 character after each character (i.e. cZaZtZ -> cat)
'F' = flip the string
'U' = ASCII shift all characters by +1
'D' = ASCII shift all characters by -1
'L' = Shift all characters to the left by 1
'R' = Shift all characters to the right by 
'''
x=0

while x<len(pattern):
    for y in pattern:
        if y=="A" or y=="a":
            updatedword=add_letters(updatedword,1)
            print("* Adding 1 letter between all characters:", updatedword)
            print()
            x+=1

        if y=="X" or y=="x":
            updatedword=delete_characters(updatedword,1)
            print("* Deleting 1 character:", updatedword)
            print()
            x+=1

        if y=="F" or y=="f":
            updatedword=flip(updatedword)
            print("* Flipping:", updatedword)
            print()
            x+=1

        if y=="U" or y=="u":
            updatedword=ascii_shift(updatedword,"up")
            print("* ASCII shifting up:", updatedword)
            print()
            x+=1

        if y=="D" or y=="d":
            updatedword=ascii_shift(updatedword,"down")
            print("* ASCII shifting down:", updatedword)
            print()
            x+=1

        if y=="L" or y=="l":
            updatedword=shift_left(updatedword)
            print("* Shifting left:", updatedword)
            print()
            x+=1

        if y=="R" or y=="r":
            updatedword=shift_right(updatedword)
            print("* Shifting right:", updatedword)
            print()
            x+=1
            
print("Final encoding/decoding: ",updatedword)
            

            
            
            


