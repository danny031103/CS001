#Assignment #2 Part 0
#Lottery winning divider program

#capture user input
winnings=float(input("How much money did you win? "))
num_of_people=int(input("How many people are splitting the winnings? "))
tax=float(input("What is the tax rate on lottery winnings (i.e. 25 = 25%): )"))


#computations and formatting
f_winnings=format(winnings, ",.2f")

win_per_person=winnings/num_of_people
f_win_per_person=format(win_per_person, ".2f")

tax_per_person=win_per_person*(tax/100)
f_tax_per_person=format(tax_per_person, ",.2f")

take_home_per_person=win_per_person-tax_per_person
f_take_home_per_person=format(take_home_per_person, ",.2f")

#generate output
print()
print("In total you won $" + f_winnings)
print("Split", num_of_people, "ways that amounts to $" + f_win_per_person + " per person")
print("Tax per person: $" + f_tax_per_person)
print("Take home amount per person: $" + f_take_home_per_person)
