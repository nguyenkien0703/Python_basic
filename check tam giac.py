def show(a,b,c):
    if a==b and b==c :
        print("Equilateral triangle")
    elif  a==b or  b==c or c==a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")





a=int(input())
b=int(input())
c=int(input())

show(a,b,c)


