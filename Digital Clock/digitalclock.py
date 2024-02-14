# function:   horizontal_line
# input:      a width value (integer) and a single character (string)
# processing: generates a single horizontal line of the desired size
# output:     returns the generated pattern (string)
def horizontal_line(width, char):
    return width * char + "\n"

# function:   vertical_line
# input:      a shift value and a height value (both integers)  and a single character (string)
# processing: generates a single vertical line of the desired height.  the line is
#             offset from the left side of the screen using the shift value
# output:     returns the generated pattern (string)
def vertical_line(shift, height, char):
    pattern = ""
    for i in range(height):
        pattern += shift * " " + char + "\n"
    return pattern

# function:   two_vertical_lines
# input:      a width value and a height value (both integers)  and a single character (string)
# processing: generates two vertical lines.  the first line is along the left side of
#             the screen. the second line is offset using the "width" value supplied
# output:     returns the generated pattern (string)
def two_vertical_lines(width, height, char):
    pattern = ""
    for i in range(height):
        pattern += char + " " * (width - 2) + char + "\n"
    return pattern

#Function to print number 0
def number_0(width,character):
    pattern=""
    pattern+=(horizontal_line(width, character))
    pattern+=two_vertical_lines(width, 3, character)
    pattern+=horizontal_line(width, character)
    return pattern

#Function to print number 1   
def number_1(width,character):
    pattern = ""
    pattern += vertical_line(width - 1, 5, character)
    return pattern

#Function to print number 2
def number_2(width, character):
    pattern=""
    pattern+=(horizontal_line(width, character))
    pattern+=vertical_line(width - 1, 1, character)
    pattern+=(horizontal_line(width, character))
    pattern+=vertical_line(0, 1, character)
    pattern+=(horizontal_line(width, character))
    return pattern

#Function to print number 3
def number_3(width,character):
    pattern=""
    pattern+=(horizontal_line(width, character))
    pattern+=vertical_line(width - 1, 1, character)
    pattern+=(horizontal_line(width, character))
    pattern+=vertical_line(width - 1, 1, character)
    pattern+=(horizontal_line(width, character))
    return pattern

#Function to print number 4
def number_4(width,character):
    pattern=""
    pattern+=two_vertical_lines(width, 2, character)
    pattern+=(horizontal_line(width, character))
    pattern+=vertical_line(width - 1, 2, character)
    return pattern

#Function to print number 5
def number_5(width,character):
    pattern=""
    pattern+=(horizontal_line(width, character))
    pattern+=vertical_line(0, 1, character)
    pattern+=(horizontal_line(width, character))
    pattern+=vertical_line(width - 1, 1, character)
    pattern+=(horizontal_line(width, character))
    return pattern


#Function to print number 6
def number_6(width,character):
    pattern=""
    pattern+=(horizontal_line(width, character))
    pattern+=vertical_line(0, 1, character)
    pattern+=(horizontal_line(width, character))
    pattern+=two_vertical_lines(width, 1, character)
    pattern+=(horizontal_line(width, character))
    return pattern

#Function to print number 7
def number_7(width,character):
    pattern=""
    pattern+=(horizontal_line(width, character))
    pattern+=vertical_line(width - 1, 4, character)
    return pattern
    
#Function to print number 8
def number_8(width,character):
    pattern=""
    pattern+=(horizontal_line(width, character))
    pattern+=two_vertical_lines(width, 1, character)
    pattern+=(horizontal_line(width, character))
    pattern+=two_vertical_lines(width, 1, character)
    pattern+=(horizontal_line(width, character))
    return pattern

#Function to print number 9
def number_9(width,character):
    pattern=""
    pattern+=(horizontal_line(width, character))
    pattern+=two_vertical_lines(width, 1, character)
    pattern+=(horizontal_line(width, character))
    pattern+=vertical_line(width - 1, 2, character)
    return pattern

def print_number(number,width,character):
    if number==0:
        printnum=""
        printnum+=number_0(width,character)
        return printnum

    elif number==1:
        printnum=""
        printnum+=number_1(width,character)
        return printnum

    elif number==2:
        printnum=""
        printnum+=number_2(width,character)
        return printnum

    elif number==3:
        printnum=""
        printnum+=number_3(width,character)
        return printnum

    elif number==4:
        printnum=""
        printnum+=number_4(width,character)
        return printnum

    elif number==5:
        printnum=""
        printnum+=number_5(width,character)
        return printnum

    elif number==6:
        printnum=""
        printnum+=number_6(width,character)
        return printnum

    elif number==7:
        printnum=""
        printnum+=number_7(width,character)
        return printnum

    elif number==8:
        printnum=""
        printnum+=number_8(width,character)
        return printnum

    elif number==9:
        printnum=""
        printnum+=number_9(width,character)
        return printnum
   
   
def plus(width,character):
    if width%2!=0:
        pattern=""
        pattern+=vertical_line(int(width/2), 2, character)
        pattern+=(horizontal_line(width, character))
        pattern+=vertical_line(int(width/2), 2, character)
        return pattern

    if width%2==0:
        if width==6:
            pattern=""
            pattern+="  "+two_vertical_lines(1, 1, character)
            pattern+="  "+two_vertical_lines(1, 1, character)
            pattern+=(horizontal_line(width, character))
            pattern+="  "+two_vertical_lines(1, 1, character)
            pattern+="  "+two_vertical_lines(1, 1, character)
            return pattern
        
        if width==8:
            pattern=""
            pattern+="   "+two_vertical_lines(1, 1, character)
            pattern+="   "+two_vertical_lines(1, 1, character)
            pattern+=(horizontal_line(width, character))
            pattern+="   "+two_vertical_lines(1, 1, character)
            pattern+="   "+two_vertical_lines(1, 1, character)
            return pattern

        if width==10:
            pattern=""
            pattern+="    "+two_vertical_lines(1, 1, character)
            pattern+="    "+two_vertical_lines(1, 1, character)
            pattern+=(horizontal_line(width, character))
            pattern+="    "+two_vertical_lines(1, 1, character)
            pattern+="    "+two_vertical_lines(1, 1, character)
            return pattern
        


def minus(width,character):
    pattern=""
    pattern+=(horizontal_line(width, character))
    return(pattern)

def mult(width,character):
    pattern=""
    pattern+=""+two_vertical_lines(width+1, 1, character)
    pattern+=" "+two_vertical_lines(width-2, 1, character)
    pattern+="  "+two_vertical_lines(width-4, 1, character)
    pattern+=" "+vertical_line(int(width/3.5), 1, character)
    pattern+="  "+two_vertical_lines(width-4, 1, character)
    pattern+=" "+two_vertical_lines(width-2, 1, character)
    pattern+=""+two_vertical_lines(width, 1, character)
    return pattern

    
def check_answer(number1, number2, answer, operator):
    if operator=="+":
        correct=number1+number2
        if answer==correct:
            return "Correct."
        if answer!=correct:
            return "Sorry, that's not correct."
    if operator=="-":
        correct=number1-number2
        if answer==correct:
            return "Correct."
        if answer!=correct:
            return "Sorry, that's not correct."
    if operator=="*":
        correct=number1*number2
        if answer==correct:
            return "Correct."
        if answer!=correct:
            return "Sorry, that's not correct."
    


    





    
