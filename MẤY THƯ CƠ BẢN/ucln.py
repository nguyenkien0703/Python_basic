
def ucln(a,b):
    while b !=0:
        r = a%b
        a=b
        b=r
    return a



a=int(input())
b=int(input())

print(ucln(a,b))


