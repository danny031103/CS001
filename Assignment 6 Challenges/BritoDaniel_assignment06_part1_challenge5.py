#Daniel Brito
#db4471
#Prof. Khye
#Assignment 6 Challenge 5

def simple_sort_version2(a,b,c):
    if (a>b) and (a>c) and (b>c):
        return(c,b,a)
    elif (a<b) and (a<c) and (b<c):
        return(a,b,c)
    elif (b>c) and (b>a) and (a>c):
        return(c,a,b)
    elif (b>c) and (b>a) and (a<c):
        return(a,c,b)
    elif (a<b) and (a<c) and (b<a):
        return(b,a,c)
    elif (a>b) and (a>c) and (b<c):
        return(b,c,a)
    elif (a==b) and (c>a):
        return (a,b,c)
    elif (a==b) and (c<a):
        return (c,a,b)
    elif (a==c) and (b>a):
        return(a,c,b)
    elif (a==c) and (b<a):
        return(b,a,c)
    elif (b==c) and (a>b):
        return(b,c,a)
    elif (b==c) and (a<b):
        return(a,b,c)

# your function should work perfectly with the following lines of code
a, b, c = simple_sort_version2(10, 20, 30)
print(a, b, c) # 10 20 30

a, b, c = simple_sort_version2(10, 30, 20)
print(a, b, c) # 10 20 30

a, b, c = simple_sort_version2(30, 20, 10)
print(a, b, c) # 10 20 30

a, b, c = simple_sort_version2(30, 20, 20)
print(a, b, c) # 20 20 30
