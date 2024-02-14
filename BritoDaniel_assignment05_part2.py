#Daniel Brito
#db4471
#Prof. Khye
#Assignment #5 Part 2

import random
import math

#User Input
num_throws=int(input("Number of throws? "))

#Input Validation
while num_throws<1:
    print("Invalid, try again!")
    num_throws=int(input("Number of throws? "))

#initial hit variables
grey_hits=0
red_hits=0
yellow_hits=0
green_hits=0
black_hits=0
blue_hits=0
mixed_hits=0
misses=0

#distance formula:
#math.sqrt(((x-h)(x-h))+((y-k)(y-k)))

#circle variables/absolute value
radius_black=100
black_h=450
black_k=200
radius_yellow=50
yellow_h=450
yellow_k=100

# perform number of throws and compute where they hit
for i in range(num_throws):
    rand_x=random.randint(0, 800)
    rand_y=random.randint(0, 500)
    
    #Distance Values for circles
    dist_black=math.sqrt(((rand_x-450)*(rand_x-450))+((rand_y-200)*(rand_y-200)))
    dist_yellow=math.sqrt(((rand_x-450)*(rand_x-450))+((rand_y-100)*(rand_y-100)))
    
#dart hits grey 
    if rand_x>200 and rand_x<250 and rand_y>200 and rand_y<250:
        grey_hits+=1

#dart hits red
    elif (rand_x>50 and rand_x<200 and rand_y>50 and rand_y<250) or (rand_x>200 and rand_x<250 and rand_y>50 and rand_y<200):
        red_hits+=1

#dart hits blue
    elif (rand_x>200 and rand_x<300 and rand_y>250 and rand_y<400) or (rand_x>250 and rand_x<300 and rand_y<250 and rand_y>200):
        blue_hits+=1

#dart hits green
    elif (rand_x>600 and rand_x<750 and rand_y>100 and rand_y<150) or (rand_x>600 and rand_x<650 and rand_y<400 and rand_y>150) or (rand_x>700 and rand_x<750 and rand_y<400 and rand_y>150) or (rand_x>600 and rand_x<750 and rand_y>400 and rand_y<450):
        green_hits+=1
        
#dart hits black
    elif dist_black<=radius_black:
        black_hits+=1
    
#dart hits yellow
    elif dist_yellow<=radius_yellow:
        yellow_hits+=1

#dart lands in covered yellow region
    elif (dist_yellow<=radius_yellow) and dist_black<=radius_black:
        mixed_hits+=1
        
#misses
    else:
        misses+=1

#Variable to account for intersecting part of circles
new_yellow_hits=yellow_hits-mixed_hits

#percentages
grey_percent=format((grey_hits/num_throws)*100, ",.2f")
red_percent=format((red_hits/num_throws)*100, ",.2f")
blue_percent=format((blue_hits/num_throws)*100, ",.2f")
green_percent=format((green_hits/num_throws)*100, ",.2f")
black_percent=format((black_hits/num_throws)*100, ",.2f")
yellow_percent=format((new_yellow_hits/num_throws)*100, ",.2f")
miss_percent=format((misses/num_throws)*100, ",.2f")

# output
print ("Red:", red_hits, "("+str(red_percent)+"%)")
print ("Blue:", blue_hits, "("+str(blue_percent)+"%)")
print ("Grey:", grey_hits, "("+str(grey_percent)+"%)")
print ("Black:", black_hits, "("+str(black_percent)+"%)")
print ("Yellow:", new_yellow_hits, "("+str(yellow_percent)+"%)")
print ("Green:", green_hits, "("+str(green_percent)+"%)")
print ("Misses:", misses, "("+str(miss_percent)+"%)")



