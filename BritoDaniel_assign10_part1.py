#Daniel Brito
#db4471
#Prof. Khye
#Assignment 10 Part 1a
##############################

#Dictionaries/Lists
valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

#Large Dictionary
pokemon = {
              'charmander': {'quantity': 3, 'fee': 100.0, 'typing': ['fire']},
              'squirtle': {'quantity': 2, 'fee': 50.0, 'typing': ['water']},
              'bulbasaur': {'quantity': 5, 'fee': 25.0, 'typing': ['grass', 'poison']},
              'gyarados': {'quantity': 1, 'fee': 1000.0, 'typing': ['water', 'flying']}
          }

#Break into smaller dictionaries for simpler appending, although the method dictionary[][] may sometimes be more useful

#Name Dictionary
pokemonname= {
                'charmander':"Charmander",
                'squirtle':"Squirtle",
                'bulbasaur':"Bulbasaur",
                'gyarados':"Gyarados"


                }

#Quantity Dictionary
pokemonquantity= {

                    'charmander':3,
                    'squirtle':2,
                    'bulbasaur':5,
                    'gyarados':1

                }

#Fee Dictionary
pokemonfee= {

                    'charmander':100.0,
                    'squirtle':50.0,
                    'bulbasaur':25.0,
                    'gyarados':1000.0

                }

#Type Dictionary
pokemontype= {

                    'charmander':'fire',
                    'squirtle':'water',
                    'bulbasaur':['grass', 'poison'],
                    'gyarados':['water', 'flying']

                }

loopvariable="yes"

while loopvariable=="yes":
    print("Welcome to the Pokemon Center!")
    menuchoice=input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ")

    #If statement for quitting the program
    if menuchoice=="q" or menuchoice=="Q":
        print("See you next time!")
        loopvariable="no"

    #If statement for removing a pokemon
    if menuchoice=="r" or menuchoice=="R":
        pokemontoremove=input("Enter name of Pokemon to remove: ")
        if pokemontoremove in pokemon:
            del pokemon[pokemontoremove]
            del pokemonfee[pokemontoremove]
            del pokemonquantity[pokemontoremove]
            del pokemontype[pokemontoremove]
            print("Pokemon removed.")
        else:
            print("Pokemon not found, cannot remove.")
            
    if menuchoice=="t" or menuchoice=="T":
        typetosearch=input("Enter Pokemon type: ")
        if typetosearch not in valid_pokemon_types:
            print("Not a valid type to search.")
            print()
        else:
            print(format("Name", "<18s"), format("Amount Available", ">20s"), format("Adoption Fee", ">22s"), format("Type", ">28s"))
            for c in pokemontype:
                if typetosearch in pokemontype[c]:
                    print(format(pokemonname[c], "<18s"), format(str(pokemonquantity[c]), ">20s"), format(str(pokemonfee[c]), ">22s")+"                        ", pokemontype[c])
            print()
                    
    if menuchoice=="l" or menuchoice=="L":
        print(format("Name", "<18s"), format("Amount Available", ">20s"), format("Adoption Fee", ">22s"), format("Type", ">28s"))
        blankstring=""
        for d in pokemon:
            print(format(pokemonname[d], "<18s"), format(str(pokemon[d]['quantity']), ">20s"), format(str(pokemon[d]['fee']), ">22s")+"                        ",(pokemontype[d]))
            print()
        
    if menuchoice=="e" or menuchoice=="E":
        maxfee=0
        for x in pokemonfee:
            if pokemonfee[x]>maxfee:
                maxfee=pokemonfee[x]
                
        minfee=100
        for y in pokemonfee:
            if pokemonfee[y]<minfee:
                minfee=pokemonfee[y]

        totaladoptfee=0
        for z in pokemonfee:
            totaladoptfee+=pokemonfee[z]
            
        highestname=""
        for a in pokemonfee:
            if pokemonfee[a]==maxfee:
                highestname=a

        lowestname=""
        for b in pokemonfee:
            if pokemonfee[b]==minfee:
                lowestname=b
        print("Highest priced Pokemon:", highestname.capitalize(), "@", maxfee, "per Pokemon")
        print("Lowest priced Pokemon:", lowestname.capitalize(), "@", minfee, "per Pokemon")
        print("Total cost to adopt all Pokemon in the Center: $"+str(totaladoptfee))
        print()

    #If statement for searching database
    if menuchoice=="s" or menuchoice=="S":
        pokemonchoice=input("Name of Pokemon to search for: ")
        pokemonchoicelower=pokemonchoice.lower()
        if pokemonchoice in pokemon:
            print("We have", pokemonquantity[pokemonchoice], pokemonchoice.capitalize(), "at the Pokemon Center")
            print("It will cost $"+str(pokemonfee[pokemonchoice]), "to adopt this Pokemon")
            print(pokemonchoice.capitalize(), "has the following type(s):", pokemontype[pokemonchoice].capitalize())
            print()

        else:
            print("We do not have any", pokemonchoice.capitalize(), "at the Pokemon Center")
            print()

    if menuchoice=="a" or menuchoice=="A":
        newpokemonname=input("Enter name of new pokemon: ")
        if newpokemonname in pokemon:
            print("Duplicate name, add operation canceled.")
        else:
            pokemon['newpokemonname']=' '
            newpokemonquantity=int(input("How many of these Pokemon are you adding? "))
            while newpokemonquantity<0 or type(newpokemonquantity)!=int:
                newpokemonquantity=input("How many of these Pokemon are you adding? ")
            pokemonquantity[newpokemonname]=newpokemonquantity
            
            newpokemonfee=float(input("What is the adoption fee for this Pokemon? "))
            while newpokemonfee<0 or type(newpokemonfee)!=float:
                newpokemonfee=input("What is the adoption fee for this Pokemon? ")
            pokemonfee[newpokemonname]=newpokemonfee
            
            print("Next you will be prompted to enter the types for this Pokemon. Pokemon can have 1 or 2 types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid type.")
            typesselectedcounter=0
            finaltype=""
            for x in range(2):
                typesselectedcounter+=1
                newtype=''
                typeselect=input("What type of Pokemon is this? ")
                x=0
                if typeselect=="help" or typeselect=="Help":
                    while x<18:
                        print("*"+valid_pokemon_types[x], end="\n" )
                        x+=1

                if (typeselect=="end" or typeselect=="End") and (typesselectedcounter==1):
                    typesselectedcounter==2

                if typeselect in valid_pokemon_types:
                    newtype+=typeselect
                    typesselectedcounter+=1
                    print("Type", typeselect, "added")

                    if typesselectedcounter==2:
                        finaltype+=(newtype+typeselect)

                if (typeselect=="end" or typeselect=="End") and typesselectedcounter==0:
                    print("You must enter at least one valid type, please try again")
                    
                print()
                pokemontype[newpokemonname]=finaltype

            pokemonname[newpokemonname]=newpokemonname
            pokemonquantity[newpokemonquantity]=newpokemonquantity
            pokemonfee[newpokemonfee]=newpokemonfee
            
'''         
        print(pokemon)
        print()
        print(pokemonquantity)
        print()
        print(pokemonfee)
        print()
        print(pokemontype)
'''

