
def max3(a,b,c):
    lonnhat =a
    if lonnhat <b:
        lonnhat=b
    if lonnhat < c:
        lonnhat=c
    return lonnhat

a=int(input())
b=int(input())
c=int(input())

print(max3(a,b,c))




