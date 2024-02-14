#Daniel Brito
#db4471
#Prof. Khye
#Assignment 06 Part 1 Challenge 3

#valid_date(month,day)
def valid_date(a,b):
    if ((a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12) and (b<=31 and b>=1)):
        return("True")
    elif ((a==4 or a==6 or a==9 or a==11) and (b<=30 and b>=1)):
        return("True")
    elif ((a==2) and (b<=28 and b>=1)):
        return("True")
    else:
        return("False")
    
#Testing
print(valid_date(99, 1))
print(valid_date(1, 99))
print(valid_date(99, 99)) 

print(valid_date(-99, 1)) 
print(valid_date(1, -99)) 
print(valid_date(-99, -99)) 

print(valid_date(9, 25)) 
print(valid_date(10, 15)) 
print(valid_date(11, 31)) 
print(valid_date(2, 28))
print(valid_date(2, 29)) 

