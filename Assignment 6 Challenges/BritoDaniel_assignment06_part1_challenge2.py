a = 5
b = 10
c = 15
d = 20
e = 20

# function:   maximum
# input:      two integers/floats
# processing: finds the maximum between two values
# output:     returns the result (float0
def maximum(a, b):
    if a-b>0:
        return(a)
    elif a==b:
        return(a)
    else:
        return(b)
    
# function:   minimum
# input:      two integers/floats
# processing: finds the maximum between two values
# output:     returns the result (float0
def minimum(a, b):
    if a-b>0:
        return(b)
    elif a==b:
        return(a)
    else:
        return(a)

ans1 = maximum(a, b)
ans2 = maximum(a, c)
ans3 = maximum(a, d)
print(ans1, ans2, ans3)

ans4 = minimum(d, c)
ans5 = minimum(d, b)
ans6 = minimum(d, a)
print(ans4, ans5, ans6)

ans7 = maximum( maximum(a, b), maximum(c, d) )
print("The biggest is:", ans7)

ans8 = maximum(d, e) 
ans8 = minimum(d, e) 
print(ans8, ans8)
