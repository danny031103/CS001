#Daniel Brito
#db4471
#Prof. Khye
#Assignment 5 Part 0

num_prices=int(input("How many prices would you like to collect? "))

while num_prices<1:
    print("Must be positive, try again.")
    num_prices=int(input("How many prices would you like to collect? "))

print("Thanks, here we go!")

#Variables
progress=0
itemnum=1
total=0

#Loop
for progress in range(num_prices):
    price=float(input("Enter price #"+str(itemnum)+": "))
    total+=price
    progress+=1
    

    while price<0:
        print("No negative prices allowed, try again")
        price=float(input("Enter price #"+str(itemnum)+":"))

    if price>0:
        itemnum+=1
        
#Variables
average=total/progress

#Print Report
print("----Report----")
print("Total:", total)
print("Average:", average)
        
