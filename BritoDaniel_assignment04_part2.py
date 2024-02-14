#Daniel Brito
#db4471
#Prof. Khye
#Helped by Sabrina (tutor)
#Rock Paper Scissor Lizard Spock Game

import random

#User Input
print("Lets Play Rock, Paper, Scissor, Lizard, Spock!")
reqwins=int(input("How many wins is required to end the tournament?(>0) "))

while reqwins<1:
    print("Invalid, try again")
    reqwins=int(input("How many wins is required to end the tournament? "))

if reqwins>0:
    print("OK, here we go")
    print()

#Variables
keepplaying="yes"
roundnum=1
userwins=0
compwins=0
ties=0
rock=1
paper=2
scissor=3
lizard=4
spock=5
compchoice=random.randint(1,5)
compchoice1="Rock"
compchoice2="Paper"
compchoice3="Scissor"
compchoice4="Lizard"
compchoice5="Spock"
rockplayed=0
paperplayed=0
scissorplayed=0
lizardplayed=0
spockplayed=0
urock=0
upaper=0
uscissor=0
ulizard=0
uspock=0

#Show Round number and game menu
while keepplaying=="yes":
    print("----------------------------------------")
    print()
    print("Round #"+str(roundnum))
    print("You have won", userwins, "rounds")
    print("The computer has won", compwins, "rounds")
    print("There have been", ties, "ties so far")
    print("----------------------------------------")
    print()
    userchoice=input("(R)ock, (P)aper, (S)cissors, (L)izard or Sp(O)ck: ")
    compchoice=random.randint(1,5)
    
    while userchoice!="R" and userchoice!="r" and userchoice!="P" and userchoice!="p" and userchoice!="S" and userchoice!="s" and userchoice!="L" and userchoice!="l" and userchoice!="O" and userchoice!="o":
        print("This is an invalid choice, please try again.")
        userchoice=input("(R)ock, (P)aper, (S)cissors, (L)izard or Sp(O)ck: ")
        
    if userchoice=="R" or userchoice=="r":
        nuserchoice=1

    elif userchoice=="P" or userchoice=="p":
        nuserchoice=2

    elif userchoice=="S" or userchoice=="s":
        nuserchoice=3

    elif userchoice=="L" or userchoice=="l":
        nuserchoice=4

    elif userchoice=="O" or userchoice=="o":
        nuserchoice=5
        
    #else:
         #print("This is an invalid choice, please try again.")
         #userchoice=input("(R)ock, (P)aper, (S)cissors, (L)izard or Sp(O)ck: ")

         
#ROCK WINS
    if nuserchoice==4 and compchoice==1:
        print("The computer has selected", compchoice1)
        print("Rock beats Lizard")
        print("Computer Wins!")
        compwins+=1
        roundnum+=1
        rockplayed+=1
        lizardplayed+=1
        ulizard+=1

    elif nuserchoice==3 and compchoice==1:
        print("The computer has selected", compchoice1)
        print("Rock beats Scissor")
        print("Computer Wins!")
        compwins+=1
        roundnum+=1
        rockplayed+=1
        scissorplayed+=1
        uscissor+=1

    elif nuserchoice==1 and compchoice==3:
        print("The computer has selected", compchoice3)
        print("Rock beats Scissor")
        print("User Wins!")
        userwins+=1
        roundnum+=1
        rockplayed+=1
        scissorplayed+=1
        urock+=1

    elif nuserchoice==1 and compchoice==4:
        print("The computer has selected", compchoice4)
        print("Rock beats Lizard")
        print("User Wins!")
        userwins+=1
        roundnum+=1
        rockplayed+=1
        lizardplayed+=1
        urock+=1

#Paper Wins
    elif nuserchoice==1 and compchoice==2:
        print("The computer has selected", compchoice2)
        print("Paper beats Rock")
        print("Computer Wins!")
        compwins+=1
        roundnum+=1
        rockplayed+=1
        paperplayed+=1
        urock+=1

    elif nuserchoice==5 and compchoice==2:
        print("The computer has selected", compchoice2)
        print("Paper beats Spock")
        print("Computer Wins!")
        compwins+=1
        roundnum+=1
        paperplayed+=1
        spockplayed+=1
        uspock+=1

    elif nuserchoice==2 and compchoice==5:
        print("The computer has selected", compchoice5)
        print("Paper beats Spock")
        print("User Wins!")
        userwins+=1
        roundnum+=1
        paperplayed+=1
        spockplayed+=1
        upaper+=1

    elif nuserchoice==2 and compchoice==1:
        print("The computer has selected", compchoice1)
        print("Paper beats Rock")
        print("User Wins!")
        userwins+=1
        roundnum+=1
        rockplayed+=1
        paperplayed+=1
        upaper+=1

#Scissor Wins
    elif nuserchoice==2 and compchoice==3:
        print("The computer has selected", compchoice3)
        print("Scissor beats Paper")
        print("Computer Wins!")
        compwins+=1
        roundnum+=1
        paperplayed+=1
        scissorplayed+=1
        upaper+=1

    elif nuserchoice==4 and compchoice==3:
        print("The computer has selected", compchoice3)
        print("Scissor beats Lizard")
        print("Computer Wins!")
        compwins+=1
        roundnum+=1
        scissorplayed+=1
        lizardplayed+=1
        ulizard+=1

    elif nuserchoice==3 and compchoice==4:
        print("The computer has selected", compchoice4)
        print("Scissor beats Lizard")
        print("User Wins!")
        userwins+=1
        roundnum+=1
        scissorplayed+=1
        lizardplayed+=1
        uscissor+=1

    elif nuserchoice==3 and compchoice==2:
        print("The computer has selected", compchoice2)
        print("Scissor beats Paper")
        print("User Wins!")
        userwins+=1
        roundnum+=1
        paperplayed+=1
        scissorplayed+=1
        uscissor+=1

#Lizard Wins
    elif nuserchoice==5 and compchoice==4:
        print("The computer has selected", compchoice4)
        print("Lizard beats Spock")
        print("Computer Wins!")
        compwins+=1
        roundnum+=1
        lizardplayed+=1
        spockplayed+=1
        uspock+=1

    elif nuserchoice==2 and compchoice==4:
        print("The computer has selected", compchoice4)
        print("Lizard beats Paper")
        print("Computer Wins!")
        compwins+=1
        roundnum+=1
        lizardplayed+=1
        paperplayed+=1
        upaper+=1

    elif nuserchoice==4 and compchoice==5:
        print("The computer has selected", compchoice5)
        print("Lizard beats Spock")
        print("User Wins!")
        userwins+=1
        roundnum+=1
        lizardplayed+=1
        spockplayed+=1
        ulizard+=1

    elif nuserchoice==4 and compchoice==2:
        print("The computer has selected", compchoice2)
        print("Lizard beats Paper")
        print("User Wins!")
        userwins+=1
        roundnum+=1
        lizardplayed+=1
        paperplayed+=1
        ulizard+=1



#Spock Wins
    elif nuserchoice==3 and compchoice==5:
        print("The computer has selected", compchoice5)
        print("Spock beats Scissor")
        print("Computer Wins!")
        compwins+=1
        roundnum+=1
        spockplayed+=1
        scissorplayed+=1
        uscissor+=1

    elif nuserchoice==1 and compchoice==5:
        print("The computer has selected", compchoice5)
        print("Spock beats Rock")
        print("Computer Wins!")
        compwins+=1
        roundnum+=1
        spockplayed+=1
        rockplayed+=1
        urock+=1

    elif nuserchoice==5 and compchoice==3:
        print("The computer has selected", compchoice3)
        print("Spock beats Scissor")
        print("User Wins!")
        userwins+=1
        roundnum+=1
        spockplayed+=1
        scissorplayed+=1
        uspock+=1

    elif nuserchoice==5 and compchoice==1:
        print("The computer has selected", compchoice1)
        print("Spock beats Rock")
        print("User Wins!")
        userwins+=1
        roundnum+=1
        spockplayed+=1
        rockplayed+=1
        uspock+=1

#Ties
    elif nuserchoice==1 and compchoice==1:
        print("The computer has selected", compchoice1)
        print("The round has ended in a tie! No points awarded!")
        roundnum+=1
        rockplayed+=2
        urock+=1
        ties+=1

    elif nuserchoice==2 and compchoice==2:
        print("The computer has selected", compchoice2)
        print("The round has ended in a tie! No points awarded!")
        roundnum+=1
        paperplayed+=2
        upaper+=1
        ties+=1

    elif nuserchoice==3 and compchoice==3:
        print("The computer has selected", compchoice3)
        print("The round has ended in a tie! No points awarded!")
        roundnum+=1
        scissorplayed+=2
        uscissor+=1
        ties+=1

    elif nuserchoice==4 and compchoice==4:
        print("The computer has selected", compchoice4)
        print("The round has ended in a tie! No points awarded!")
        roundnum+=1
        lizardplayed+=2
        ulizard+=1
        ties+=1

    elif nuserchoice==5 and compchoice==5:
        print("The computer has selected", compchoice5)
        print("The round has ended in a tie! No points awarded!")
        roundnum+=1
        spockplayed+=2
        uspock+=1
        ties+=1
        
#End Game
    if userwins==reqwins:
        print("User Wins the game!")
        keepplaying="no"
        print()

    if compwins==reqwins:
        print("Computer Wins the game!")
        keepplaying="no"
        print()      


#Game Results
crock=rockplayed-urock
cpaper=paperplayed-upaper
cscissor=scissorplayed-uscissor
clizard=lizardplayed-ulizard
cspock=spockplayed-uspock

print("Game summary:")
print("Rock was played", rockplayed, "times" "(User="+str(urock)+";", "Computer="+str(crock))
print("Paper was played", paperplayed, "times" "(User="+str(upaper)+";", "Computer="+str(cpaper))
print("Scissors was played",scissorplayed, "times" "(User="+str(uscissor)+";", "Computer="+str(cscissor))
print("Lizard was played", lizardplayed, "times" "(User="+str(ulizard)+";", "Computer="+str(clizard))
print("Spock was played", spockplayed, "times" "(User="+str(uspock)+";", "Computer="+str(cspock))



