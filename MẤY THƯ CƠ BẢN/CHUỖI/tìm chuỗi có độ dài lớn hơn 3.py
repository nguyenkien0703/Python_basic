
'''CACSH 1 '''
s=input()
lst=[]
a=s.split()
for i in a :
    if len(i)>3:
        lst.append(i)
print(lst)
'''CACSH 2 '''
str = str(input())

def check(str):
    arr = []
    lst =  str.split(" ")
    for i in range(len(lst)):
        if len(lst[i]) > 3:
            arr.append(lst[i])
    return arr

print(check(str))





