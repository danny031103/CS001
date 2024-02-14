#Daniel Brito
#db4471
#Prof. Khye
#Pokemon Database

# Pokemon information and variables
pokemon_names=['charmander', 'squirtle', 'bulbasaur', 'gyarados']
pokemon_amounts=[3, 2, 5, 1]
adoption_fees = [100.00, 50.00, 25.00, 1000.00]
pokemon_types = [['fire'], ['water'], ['grass', 'poison'], ['water', 'flying']]
valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']
typesselectedcounter=0
typess=[]
addedtypes=''
newaddedtypes=''

[x.lower() for x in pokemon_names]

#Loop to keep the program running until user quits
while True:
    print("Welcome to the Pokemon Center!")
    selection=input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ")

#Quit program
    if selection=="q" or selection=="Q":
        print('See you next time!')
        break

#Search function
    if selection=="s" or selection=="S":
        pokemon=input("Name of Pokemon to search for: ")
        pokemonc=pokemon.lower()
        capital_pokemon = pokemonc.capitalize()
        if pokemonc in pokemon_names:
            location=pokemon_names.index(pokemonc)
            amount=pokemon_amounts[location]
            print("We have", pokemon_amounts[location], capital_pokemon, "at the Pokemon Center")
            print("It will cost $"+str(adoption_fees[location]), "to adopt this Pokemon")
            print(capital_pokemon, "has the following type(s):", pokemon_types[location])
            print()

        else:
            pokemond=pokemonc.capitalize()
            print("We do not have any", pokemond, "at the Pokemon Center")
            print()

#Error if user inputs a command that isnt listed 
    if selection!="s" and selection!="S" and selection!="a" and selection!="A" and selection!="r" and selection!="R" and selection!="e" and selection!="E" and selection!="t" and selection!="T" and selection!="L" and selection!="l":
        print("Unknown command, please try again")
        print()

#List function

    if selection=="l" or selection=="L":
        Name="Name"
        Amount_Available="Amount Available"
        Adoption_Fee="Adoption Fee"
        Type_="Type"
        print(format(Name, "<18s"), format(Amount_Available, ">20s"), format(Adoption_Fee, ">22s"), format(Type_, ">28s"))

        for x in range(len(pokemon_names)):
            type_string = ""
            if len(pokemon_types[x]) == 1:
                type_string += pokemon_types[x][0].capitalize()
            elif len(pokemon_types[x]) == 2:
                type_string += pokemon_types[x][0].capitalize()
                type_string+=", "
                type_string += pokemon_types[x][1].capitalize()

            
                
            print(format(str.capitalize(pokemon_names[x]), "<18s"), format(str(pokemon_amounts[x]), ">20s"), format(str(adoption_fees[x]), ">22s"), format(str(type_string), ">28s"))
            
#Search based on type function
    if selection=="T" or selection=="t":
        searchtype=input("Enter Pokemon type: ")
        Name="Name"
        Amount_Available="Amount Available"
        Adoption_Fee="Adoption Fee"
        Type_="Type"
        if searchtype=="water" or searchtype=="Water":
            print(format(Name, "<18s"), format(Amount_Available, ">20s"), format(Adoption_Fee, ">22s"), format(Type_, ">28s"))
            print(format(str.capitalize(pokemon_names[-3]), "<18s"), format(str(pokemon_amounts[-3]), ">20s"), format(str(adoption_fees[-3]), ">22s"), format(str(pokemon_types[-3]), ">28s"))
            print(format(str.capitalize(pokemon_names[-1]), "<18s"), format(str(pokemon_amounts[-1]), ">20s"), format(str(adoption_fees[-1]), ">22s"), format(str(pokemon_types[-1]), ">28s"))
            
        if searchtype=="fire" or searchtype=="Fire":
            print(format(Name, "<18s"), format(Amount_Available, ">20s"), format(Adoption_Fee, ">22s"), format(Type_, ">28s"))
            print(format(str.capitalize(pokemon_names[-4]), "<18s"), format(str(pokemon_amounts[-4]), ">20s"), format(str(adoption_fees[-4]), ">22s"), format(str(pokemon_types[-4]), ">28s"))

        if searchtype=="flying" or searchtype=="flying":
            print(format(Name, "<18s"), format(Amount_Available, ">20s"), format(Adoption_Fee, ">22s"), format(Type_, ">28s"))
            print(format(str.capitalize(pokemon_names[-1]), "<18s"), format(str(pokemon_amounts[-1]), ">20s"), format(str(adoption_fees[-1]), ">22s"), format(str(pokemon_types[-1]), ">28s"))
            
        if searchtype=="grass" or searchtype=="Grass":
            print(format(Name, "<18s"), format(Amount_Available, ">20s"), format(Adoption_Fee, ">22s"), format(Type_, ">28s"))
            print(format(str.capitalize(pokemon_names[-2]), "<18s"), format(str(pokemon_amounts[-2]), ">20s"), format(str(adoption_fees[-2]), ">22s"), format(str(pokemon_types[-2]), ">28s"))

        if searchtype=="poison" or searchtype=="Poison":
            print(format(Name, "<18s"), format(Amount_Available, ">20s"), format(Adoption_Fee, ">22s"), format(Type_, ">28s"))
            print(format(str.capitalize(pokemon_names[-2]), "<18s"), format(str(pokemon_amounts[-2]), ">20s"), format(str(adoption_fees[-2]), ">22s"), format(str(pokemon_types[-2]), ">28s"))

        if searchtype not in valid_pokemon_types:
            print("We have no Pokemon of that type at our Pokemon Center")

#Add function
    if selection=="a" or selection=="A":
        newpoke=input("Enter name of new pokemon: ")
        typesselectedcounter=0
        
        if newpoke in pokemon_names:
            print("Duplicate name, add operation cancelled.")

        else:
            pokemon_names+=[newpoke]
            numnew=int(input("How many of these Pokemon are you adding? "))
            while numnew<1:
                print("Invalid, please try again")
                numnew=int(input("How many of these Pokemon are you adding? "))
            pokemon_amounts+=[numnew]

            newadopt=float(input("What is the adoption fee for this Pokemon? "))
            while newadopt<1:
                print("Invalid, please try again")
                newadopt=float(input("What is the adoption fee for this Pokemon? "))
            adoption_fees+=[newadopt]
                
            print("Next you will be prompted to enter the types for this Pokemon. Pokemon can have 1 or 2 types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid type")

            for x in range(2):
                typesselectedcounter+=1
                newtype=[]
                
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

                addedtypes+=typeselect+", "
                if (typeselect=="end" or typeselect=="End") and typesselectedcounter==0:
                    print("You must enter at least one valid type, please try again")
                    

            for c in addedtypes[0:len(addedtypes)-2]:
                newaddedtypes+=c
            newaddedtypes =[newaddedtypes]

            print(newaddedtypes)

            pokemon_types+=[newaddedtypes]

            print(pokemon_types)
            
            
                
                
                
            print("Pokemon Added!")

#Remove function          
    if selection=="R" or selection=="r":
        removename=str(input("Enter name of Pokemon to remove: "))
        if removename in pokemon_names:
            nameloc=pokemon_names.index(removename)
            del pokemon_names[nameloc]
            del pokemon_amounts[nameloc]
            del adoption_fees[nameloc]
            del pokemon_types[nameloc]
            print("Pokemon removed")

        else:
            print("Pokemon not found, cannot remove")

#Report Function
    if selection=="e" or selection=="E":
        highestprice=max(adoption_fees)
        lowestprice=min(adoption_fees)
        exppoke=adoption_fees.index(highestprice)
        cheappoke=adoption_fees.index(lowestprice)
        sumofpokes=sum(adoption_fees)
        
        print("Highest priced pokemon:", pokemon_names[exppoke].capitalize() ,"@",highestprice , "per Pokemon")
        print("Lowest priced pokemon:", pokemon_names[cheappoke].capitalize() ,"@",lowestprice , "per Pokemon")
        print("Total cost to adopt all Pokemon in the Center:", sumofpokes)
        print()
        


