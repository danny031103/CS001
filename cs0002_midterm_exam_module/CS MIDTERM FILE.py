import cs0002_midterm_exam_module
input = cs0002_midterm_exam_module.redefine_input("M040184")

# your program goes below this line
total=0
num = ''
while num != "end" :
    num=input("Enter a number:")
    total+=int(num)
    print(total)

    if num=="end":
        break


    
    
