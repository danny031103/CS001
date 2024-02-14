#Daniel Brito
#Assignment 3 Part 2
#Prof. Khye

user_date=int(input("Please enter a date:(YYYYMMDD): "))
day=user_date%100
month=((((user_date-day)%100000)//100)%100)
year=(((user_date)-(month*100)+day))//10000
sday=str(day)


if year%4==0 and year%100!=0 and year%400!=0:
    print(year, "is a leap year!")

else:
    print(year, "is not a leap year!")    

#USER INPUT DATE
if user_date <99999999:
    day=user_date%100
    month=((((user_date-day)%100000)//100)%100)
    year=(((user_date)-(month*100)+day))//10000
    sday=str(day)
    iday=int(day)

#INVALID DATES

    if (day <=0 or day >=32)or (month <1 or month >12):
        print("This is NOT a valid date in", year)
        

#FEBRUARY
    elif month == 2:
        if month == 2 and day >=29:
            print("This is NOT a valid date.")
        if month == 2 and day <=28:
            if day == 1 or day == 21 or day == 31:
                day= str(day)+ "st,"
                print("February", day, year, "is a valid date")
            elif day == 2 or day == 22:
                day= str(day)+ "nd,"
                print("February", day, year, "is a valid date")
            elif day == 3 or day ==23:
                day= str(day) + "rd,"
                print("February", day, year, "is a valid date")
            else:
                day= str(day) + "th,"
                print("February", day, year, "is a valid date")


#30 DAY MONTHS
    elif month <=11:
        if (month == 4 or month == 6 or month == 9 or month == 11) and day >=31:
            print("This is NOT a valid date.")
        if month == 4 and day <=30:
            if day == 1 or day == 21 or day == 31:
                day= str(day)+ "st,"
                print("April", day, year, "is a valid date")
            elif day == 2 or day == 22:
                day= str(day)+ "nd,"
                print("April", day, year, "is a valid date")
            elif day == 3 or day ==23:
                day= str(day) + "rd,"
                print("April", day, year, "is a valid date")
            else:
                day= str(day) + "th,"
                print("April", day, year, "is a valid date")
        elif month == 6 and day <=30:
            if day == 1 or day == 21 or day == 31:
                day= str(day)+ "st,"
                print("June", day, year, "is a valid date")
            elif day == 2 or day == 22:
                day= str(day)+ "nd,"
                print("June", day, year, "is a valid date")
            elif day == 3 or day ==23:
                day= str(day) + "rd,"
                print("June", day, year, "is a valid date")
            else:
                day= str(day) + "th,"
                print("June", day, year, "is a valid date")
        elif  month == 9 and day <=30:
            if day == 1 or day == 21 or day == 31:
                day= str(day)+ "st,"
                print("September", day, year, "is a valid date")
            elif day == 2 or day == 22:
                day= str(day)+ "nd,"
                print("September", day, year, "is a valid date")
            elif day == 3 or day ==23:
                day= str(day) + "rd,"
                print("September", day, year, "is a valid date")
            else:
                day= str(day) + "th,"
                print("September", day, year, "is a valid date")
        elif month == 11 and day <=30:
            if day == 1 or day == 21 or day == 31:
                day= str(day)+ "st,"
                print("November", day, year, "is a valid date")
            elif day == 2 or day == 22:
                day= str(day)+ "nd,"
                print("November", day, year, "is a valid date")
            elif day == 3 or day ==23:
                day= str(day) + "rd,"
                print("November", day, year, "is a valid date")
            else:
                day= str(day) + "th,"
                print("November", day, year, "is a valid date")
#31 DAY MONTHS 

    if month <= 12:
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day >=32:
            print("This is NOT a valid date.")
        if month == 1 and day <=31:
            if day == 1 or day == 21 or day == 31:
                day= str(day)+ "st,"
                print("January", day, year, "is a valid date")
            elif day == 2 or day == 22:
                day= str(day)+ "nd,"
                print("January", day, year, "is a valid date")
            elif day == 3 or day ==23:
                day= str(day) + "rd,"
                print("January", day, year, "is a valid date")
            else:
                day= str(day) + "th,"
                print("January", day, year, "is a valid date")
        elif month == 3 and day <=31:
            if day == 1 or day == 21 or day == 31:
                day= str(day)+ "st,"
                print("March", day, year, "is a valid date")
            elif day == 2 or day == 22:
                day= str(day)+ "nd,"
                print("March", day, year, "is a valid date")
            elif day == 3 or day ==23:
                day= str(day) + "rd,"
                print("March", day, year, "is a valid date")
            else:
                day= str(day) + "th,"
                print("March", day, year, "is a valid date")
        elif  month == 5 and day <=31:
            if day == 1 or day == 21 or day == 31:
                day= str(day)+ "st,"
                print("May", day, year, "is a valid date")
            elif day == 2 or day == 22:
                day= str(day)+ "nd,"
                print("May", day, year, "is a valid date")
            elif day == 3 or day ==23:
                day= str(day) + "rd,"
                print("May", day, year, "is a valid date")
            else:
                day= str(day) + "th,"
                print("May", day, year, "is a valid date")
        elif month == 7 and day <=31:
            if day == 1 or day == 21 or day == 31:
                day= str(day)+ "st,"
                print("July", day, year, "is a valid date")
            elif day == 2 or day == 22:
                day= str(day)+ "nd,"
                print("July", day, year, "is a valid date")
            elif day == 3 or day ==23:
                day= str(day) + "rd,"
                print("July", day, year, "is a valid date")
            else:
                day= str(day) + "th,"
                print("July", day, year, "is a valid date")
        elif month == 8 and day <=31:
            if day == 1 or day == 21 or day == 31:
                day= str(day)+ "st,"
                print("August", day, year, "is a valid date")
            elif day == 2 or day == 22:
                day= str(day)+ "nd,"
                print("August", day, year, "is a valid date")
            elif day == 3 or day ==23:
                day= str(day) + "rd,"
                print("August", day, year, "is a valid date")
            else:
                day= str(day) + "th,"
                print("August", day, year, "is a valid date")
        elif  month == 10 and day <=31:
            if day == 1 or day == 21 or day == 31:
                day= str(day)+ "st,"
                print("October", day, year, "is a valid date")
            elif day == 2 or day == 22:
                day= str(day)+ "nd,"
                print("October", day, year, "is a valid date")
            elif day == 3 or day ==23:
                day= str(day) + "rd,"
                print("October", day, year, "is a valid date")
            else:
                day= str(day) + "th,"
                print("October", day, year, "is a valid date")
        elif month == 12 and day <=31:
            if day == 1 or day == 21 or day == 31:
                day= str(day)+ "st,"
                print("December", day, year, "is a valid date")
            elif day == 2 or day == 22:
                day= str(day)+ "nd,"
                print("December", day, year, "is a valid date")
            elif day == 3 or day ==23:
                day= str(day) + "rd,"
                print("December", day, year, "is a valid date")
            else:
                day= str(day) + "th,"
                print("December", day, year, "is a valid date")

#hemisphere section
dayy=user_date%100
if (month>13 or dayy>31):
    print("Cannot determine season for invalid date")

elif (month<13 and month>0 and dayy<32):
    hemisphere=input("Which hemisphere are you located in? (N)orth or (S)outh ")

    if (hemisphere=="N" or hemisphere=="n") and (month==12 or month==1 or month==2):
        print("The season on this date is Winter")

    elif (hemisphere=="N" or hemisphere=="n") and (month==5 or month==4 or month==3):
        print("The season on this date is Spring")
        
    elif (hemisphere=="N" or hemisphere=="n") and (month==6 or month==7 or month==8):
        print("The season on this date is Summer")

    elif (hemisphere== "N" or hemisphere=="n") and (month==9 or month==10 or month==11):
        print("The season on this date is Autumn")

    elif (hemisphere=="S"or hemisphere=="s") and (month==12 or month==1 or month==2):
        print("The season on this date is Summer")

    elif (hemisphere=="S" or hemisphere=="s") and (month==5 or month==4 or month==3):
        print("The season on this date is Autumn")
        
    elif (hemisphere=="S" or hemisphere=="s") and (month==6 or month==7 or month==8):
        print("The season on this date is Winter")

    elif (hemisphere=="S" or hemisphere=="s") and (month==9 or month==10 or month==11):
        print("The season on this date is Spring")

    else:
        print("Invalid entry, cannot determine season")



