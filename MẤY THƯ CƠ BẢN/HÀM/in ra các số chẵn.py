n = int(input())

lst =[]
for i in range(n):
    lst.append(int(input()))

ans =[]
for i in lst:
    if i%2==0:
        ans.append(i)
print(ans)