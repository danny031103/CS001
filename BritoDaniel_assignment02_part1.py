print("*"*50)
print("        3 Year Bank Account Balance Forecast       ")
print("*"*50)
print("This program will project how much you could earn by investing money in a bank account that pays out interest on a yearly basis.")

print()

#Collect user input for year 1
yr_1_deposit=float(input("To begin, enter how much money you would like to initially invest (i.e. 5000): "))
expected_interest_yr1=float(input("Next, enter the expected interest rate for year 2. For example, enter 5 for 5%: "))
interest_earned_yr1=(yr_1_deposit)*(expected_interest_yr1/100)
tax_rate_yr1=float(input("Finally, enter the tax rate on any interest earned this year. For example, enter 15.5 for 15.5%: "))
tax_rate_percent_year1=tax_rate_yr1/100
tax_on_interest_yr1=interest_earned_yr1-(interest_earned_yr1*tax_rate_percent_year1)
interest_earned_withtax_yr1=interest_earned_yr1-(interest_earned_yr1*(tax_rate_percent_year1))
tax_on_interest_yr1=interest_earned_yr1-interest_earned_withtax_yr1
end_balance_yr1=(yr_1_deposit)+(interest_earned_yr1)-(tax_on_interest_yr1)

print()

#Collect user input for year 2
yr_2_deposit=float(input("To begin, enter how much money you would like to initially invest (i.e. 5000): "))
expected_interest_yr2=float(input("Next, enter the expected interest rate for year 2. For example, enter 5 for 5%: "))
interest_earned=((end_balance_yr1+yr_2_deposit)*(expected_interest_yr2/100))
tax_rate_yr2=float(input("Finally, enter the tax rate on any interest earned this year. For example, enter 15.5 for 15.5%: "))
tax_rate_percent_year2=tax_rate_yr2/100
tax_on_interest=interest_earned-(interest_earned*tax_rate_percent_year2)
interest_earned_withtax_yr2=interest_earned-(interest_earned*(tax_rate_percent_year2))
tax_on_interest_yr2=interest_earned-interest_earned_withtax_yr2
end_balance_yr2=(end_balance_yr1)+(yr_2_deposit)+(interest_earned)-(tax_on_interest_yr2)

print()

#Collect user input for year 3
yr_3_deposit=float(input("To begin, enter how much money you would like to initially invest (i.e. 5000): "))
expected_interest_yr3=float(input("Next, enter the expected interest rate for year 2. For example, enter 5 for 5%: "))
interest_earned_yr3=((end_balance_yr2+yr_3_deposit)*(expected_interest_yr3/100))
tax_rate_yr3=float(input("Finally, enter the tax rate on any interest earned this year. For example, enter 15.5 for 15.5%: "))
tax_rate_percent_year3=tax_rate_yr3/100
tax_on_interest_yr3=interest_earned_yr3-(interest_earned_yr3*tax_rate_percent_year3)
interest_earned_withtax_yr3=interest_earned_yr3-(interest_earned_yr3*(tax_rate_percent_year3))
tax_on_interest_yr3=interest_earned_yr3-interest_earned_withtax_yr3
end_balance_yr3=(end_balance_yr2)+(yr_3_deposit)+(interest_earned_yr3)-(tax_on_interest_yr3)

print()

#Formatted Numbers:
fyr_1_deposit=format(yr_1_deposit, ",.2f")
finterest_earned_yr1=format(interest_earned_yr1, ",.2f")
ftax_on_interest_yr1=format(tax_on_interest_yr1, ",.2f")
fend_balance_yr1=format(end_balance_yr1, ",.2f")

fend_balance_yr1=format(end_balance_yr1, ",.2f")
fyr_2_deposit=format(yr_2_deposit, ",.2f")
finterest_earned=format(interest_earned, ",.2f")
ftax_on_interest_yr2=format(tax_on_interest_yr2, ",.2f")
fend_balance_yr2=format(end_balance_yr2, ",.2f")

fend_balance_yr2=format(end_balance_yr2, ",.2f")
fyr_3_deposit=format(yr_3_deposit, ",.2f")
finterest_earned_yr3=format(interest_earned_yr3, ",.2f")
ftax_on_interest_yr3=format(tax_on_interest_yr3, ",.2f")
fend_balance_yr3=format(end_balance_yr3, ",.2f")

#string format
sfyr_1_deposit=str(fyr_1_deposit)
sfinterest_earned_yr1=str(finterest_earned_yr1)
sftax_on_interest_yr1=str(ftax_on_interest_yr1)
sfend_balance_yr1=str(fend_balance_yr1)

sfend_balance_yr1=str(fend_balance_yr1)
sfyr_2_deposit=str(fyr_2_deposit)
sfinterest_earned=str(finterest_earned)
sftax_on_interest_yr2=str(ftax_on_interest_yr2)
sfend_balance_yr2=str(fend_balance_yr2)

sfend_balance_yr2=str(fend_balance_yr2)
sfyr_3_deposit=str(fyr_3_deposit)
sfinterest_earned_yr3=str(finterest_earned_yr3)
sftax_on_interest_yr3=str(ftax_on_interest_yr3)
sfend_balance_yr3=str(fend_balance_yr3)

#String Length
fsfyr_1_deposit=format(sfyr_1_deposit, "<20s")
fsfinterest_earned_yr1=format(sfinterest_earned_yr1, "<20s")
fsftax_on_interest_yr1=format(sftax_on_interest_yr1, "<20s")
fsfend_balance_yr1=format(sfend_balance_yr1, "<20s")
zero=format("0", "<20s") 

fsfend_balance_yr1=format(sfend_balance_yr1, "<20s")
fsfyr_2_deposit=format(sfyr_2_deposit, "<20s")
fsfinterest_earned=format(sfinterest_earned, "<20s")
fsftax_on_interest_yr2=format(sftax_on_interest_yr2, "<20s")
fsfend_balance_yr2=format(sfend_balance_yr2, "<20s")

fsfend_balance_yr2=format(sfend_balance_yr2, "<20s")
fsfyr_3_deposit=format(sfyr_3_deposit, "<20s")
fsfinterest_earned_yr3=format(sfinterest_earned_yr3, "<20s")
fsftax_on_interest_yr3=format(sftax_on_interest_yr3, "<20s")
fsfend_balance_yr3=format(sfend_balance_yr3, "<20s")

year=format("Year", "<10s")
starting_balance=format("Starting Balance", "<10s")
deposit=format("Deposit", "<10s")
interest_earned=format("Interest Earned", "<10s")
tax_on_interest=format("Tax on Interest", "<10s")
ending_balance=format("Ending Balance", "<10s")
one=format("1", "<20s")
two=format("2", "<20s")
three=format("3", "<20s")

print("--- YOUR FORECAST ---")
print()
# generate formatted output
# < (left align), > (right align), ^ (center align) 
print( format(year, "<15s"), format(starting_balance, "^18s"), "  "+format(deposit, "^20s"), format(interest_earned, "^20s"), format(tax_on_interest, "^20s"), format(ending_balance, "^20s") )
print( format(one, "<15s"), format(zero, "^18s"), format(fsfyr_1_deposit, "<20s"), format(fsfinterest_earned_yr1, "^20s"), format(fsftax_on_interest_yr1, "^20s"), format(fsfend_balance_yr1, "^20s") )
print( format(two, "<15s"), format(fsfend_balance_yr1, "^18s"), format(fsfyr_2_deposit, "<20s"), format(fsfinterest_earned, "^20s"), format(fsftax_on_interest_yr2, "^20s"), format(fsfend_balance_yr2, "^20s") )
print( format(three, "<15s"), format(fsfend_balance_yr2, "^18s"), format(fsfyr_3_deposit, "<20s"), format(fsfinterest_earned_yr3, "^20s"), format(fsftax_on_interest_yr3, "^20s"), format(fsfend_balance_yr3, "^20s") )

#Convert String values to floats for addition
print()
'''
ffsfinterest_earned_yr3=float(fsfinterest_earned_yr3)
ffsfinterest_earned=float(fsfinterest_earned)
ffsfinterest_earned_yr1=float(fsfinterest_earned_yr1)
'''
sum1=(yr_1_deposit)*(expected_interest_yr1/100)
sum2=((end_balance_yr1+yr_2_deposit)*(expected_interest_yr2/100))
sum3=((end_balance_yr2+yr_3_deposit)*(expected_interest_yr3/100))
#print sums
totdep12=yr_1_deposit+yr_2_deposit
totdepall=format(totdep12+yr_3_deposit, ",.2f")
print("Total deposited:",totdepall)
sumz12=sum1+sum2
sumzall=format(sumz12+sum3, ",.2f")
print("Total Interest earned:",sumzall)
ttd=format(tax_on_interest_yr3+tax_on_interest_yr2+tax_on_interest_yr1, ",.2f")
print("Total tax due", ttd)


