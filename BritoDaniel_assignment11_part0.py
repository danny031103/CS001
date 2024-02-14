#Daniel Brito
#db4471
#Prof. Khye
#Assignment 11 Part 0
#####################

import random

class Gumball_Machine:
    def __init__(self, num):
        self.capacity=num
        self.money=0

        self.gumball_list=[]
        
        color_choices=['red','green','blue']

        for i in range(self.capacity):
            rand_num=random.randint(0,2)
            self.gumball_list.append(color_choices[rand_num])

        print("Gumball Machine created with", self.capacity, "random gumballs.")

    def dispense(self, coin):
        # if the coin value is 0.25 and there is gumball left in the machine
        if coin == 0.25 and len(self.gumball_list) > 0:
            print("\nAccepting {}; Dispensing a {} gumball".format(coin, self.gumball_list.pop()))
            self.money += coin
        elif coin != 0.25:
            print("\nInvalid coin, no gumball will be dispensed")
        else:
            print("\nMachine is empty, no gumball will be dispensed")

    def report(self):
        print("Gumball Machine Report:")
        print("* Gumballs in machine:", self.capacity)
        print("* Money in machine: $"+format(self.money, ".2f"))

    def count_gumballs_by_color(self,color):
        num_remaining=0
        for item in self.gumball_list:
            if item==color:
                num_remaining+=1
        print(num_remaining, color, "gumball(s) can be found in the machine.")
        
        

# TESTER CODE
machine = Gumball_Machine(5)
machine.report()

machine.count_gumballs_by_color("red")
machine.count_gumballs_by_color("green")
machine.count_gumballs_by_color("blue")

machine.dispense(0.10)
machine.dispense(0.50)
machine.dispense(0.01)

machine.report()

machine.count_gumballs_by_color("red")
machine.count_gumballs_by_color("green")
machine.count_gumballs_by_color("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_color("red")
machine.count_gumballs_by_color("green")
machine.count_gumballs_by_color("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_color("red")
machine.count_gumballs_by_color("green")
machine.count_gumballs_by_color("blue")



  
        

