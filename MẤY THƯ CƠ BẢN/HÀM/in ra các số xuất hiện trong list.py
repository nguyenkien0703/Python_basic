def xuathien(lst):
    ans =[]
    for i in lst:
        if i not in ans :
            ans.append(i)
    return ans 

n =int(input())
lst =[]
for i in range(n):
    lst.append(int(input()))
print(xuathien(lst))