n =int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))

ketqua=[]
for v in lst:
    if v%2==1:
        ketqua.append(int(v))
print(ketqua)


