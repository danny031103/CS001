#Daniel Brito
#db4471
#Prof. Khye
#In class warm-up

#User Inputs
first_num= int(input("First Number? "))
second_num = int(input("Second Number? "))

#Data Checking
while second_num <= 0 or first_num<=0:
    print ("Invalid entry, try again!")
    first_num = int(input("First Number? "))
    second_num = int(input("Second Number? "))

#Top Half
accumulator = first_num
while accumulator < second_num:
    print("*"*accumulator)
    accumulator += 1

#Bottom Half
accumulator = second_num
while accumulator >= first_num:
    print("*"*accumulator)
    accumulator -= 1
