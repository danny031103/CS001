#Daniel Brito
#Assignment 2 Part 2
#Number Gymnastics

three_digit_number_1=int(input("Enter a 3 digit number between 000 and 999: "))
three_digit_number_2=int(input("Enter a 3 digit number between 000 and 999: "))

#Digits numbered from right to left (ones is 1, tens is 2, hundreds is 3)
dig_1_num1= three_digit_number_1%10
dig_2_num1= int(((three_digit_number_1%100)-dig_1_num1)/10)
dig_3_num1= int(((three_digit_number_1%1000)-(dig_1_num1+dig_2_num1))/100)              

dig_1_num2= three_digit_number_2%10
dig_2_num2= int(((three_digit_number_2%100)-dig_1_num2)/10)
dig_3_num2= int(((three_digit_number_2%1000)-(dig_1_num2+dig_2_num2))/100)
                           
print("Digits in the 1's place:", dig_1_num1, "and", dig_1_num2)
print("Digits in the 10's place:", dig_2_num1, "and", dig_2_num2)
print("Digits in the 100's place:", dig_3_num1, "and", dig_3_num2)

print()
new_dig_1_num1=str(dig_1_num1)
new_dig_2_num1=str(dig_2_num1)
new_dig_3_num1=str(dig_3_num1)
 
new_dig_1_num2=str(dig_1_num2)
new_dig_2_num2=str(dig_2_num2)
new_dig_3_num2=str(dig_3_num2)
 
print("Graphical representation of your numbers")
hundreds=format("Hundreds", "<10s")
tens=format("Tens", "<10s")
ones=format("Ones", "<10s")
print(hundreds, tens, ones)
x=dig_1_num1
y=dig_2_num1
z=dig_3_num1
a=dig_1_num2
b=dig_2_num2
c=dig_3_num2

new_1=format(z*new_dig_3_num1, "<10s")
new_2=format(y*new_dig_2_num1, "<10s")
new_3=format(x*new_dig_1_num1, "<10s")
new_4=format(a*new_dig_1_num2, "<10s")
new_5=format(b*new_dig_2_num2, "<10s")
new_6=format(c*new_dig_3_num2, "<10s")


print(new_1,new_2,new_3)
print(new_6,new_5,new_4)
'''
print(z*new_dig_3_num1,y*new_dig_2_num1,x*new_dig_1_num1)
print(a*new_dig_3_num2,b*new_dig_2_num2,c*new_dig_1_num2)
'''
print()
print("Computing Your Super Number!")
print()

#Step1
print("Step #1: Add Each Place Value")
print("- Hundreds: ", dig_3_num1, "and", dig_3_num2, "=", dig_3_num1+dig_3_num2)
print("- Tens: ", dig_2_num1, "and", dig_2_num2, "=", dig_2_num1+dig_2_num2)
print("- Ones: ", dig_1_num1, "and", dig_1_num2, "=", dig_1_num1+dig_1_num2)

sum_of_hundreds=dig_3_num1+dig_3_num2
sum_of_tens=dig_2_num1+dig_2_num2
sum_of_ones=dig_1_num1+dig_1_num2

string_sumhundreds=str(sum_of_hundreds)
string_sumtens=str(sum_of_tens)
string_sumones=str(sum_of_ones)

print()

#Step2
print("Step #2: Combine New Values")
print("- ", string_sumhundreds, "+", string_sumtens, "+", string_sumones, "=", string_sumhundreds+string_sumtens+string_sumones)

#Step3
print()
sum_of_num1_digits=dig_1_num1+dig_2_num1+dig_3_num1
print("Step #3: Compute The Sum of All Digits in First Number")
print("- ", new_dig_3_num1, "+", new_dig_2_num1, "+",new_dig_1_num1, "=", sum_of_num1_digits)

#Step4
print()
sum_of_num2_digits=dig_1_num2+dig_2_num2+dig_3_num2
print("Step #4: Compute The Sum of All Digits in Second Number")
print("- ", new_dig_3_num2, "+", new_dig_2_num2, "+",new_dig_1_num2, "=", sum_of_num2_digits)

string_sum_of_num1_digits=str(sum_of_num1_digits)
string_step_two=str(string_sumhundreds+string_sumtens+string_sumones)
string_sum_of_num2=str(sum_of_num2_digits)

print()
print("Step #5: Combine The Numbers In This Order -- Step 3 + Step 2 + Step 4")
print(string_sum_of_num1_digits+string_step_two+string_sum_of_num2)


