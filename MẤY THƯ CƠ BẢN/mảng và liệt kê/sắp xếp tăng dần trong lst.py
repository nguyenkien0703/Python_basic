#  dùng hàm có sẵn
# n =int(input())
# lst=[]
# for i in range(n):
#     lst.append(int(input()))

# lst.sort()
# print(lst)

# ko dùng hàm có sẵn
n =int(input())
lst =[]
for i in range(n):
    lst.append(int(input()))

for i in range(n):
    for j in range(i):
        if lst[i]< lst[j]:
            tmp =lst[i]
            lst[i]=lst[j]
            lst[j]=tmp

print(lst)
