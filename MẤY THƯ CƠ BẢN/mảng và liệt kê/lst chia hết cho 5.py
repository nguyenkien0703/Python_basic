'''

Cho một list các số nguyên n phần tử lst được nhập vào từ bàn phím, bạn hãy viết chương trình hiển thị ra màn hình một list chứa các số chia hết cho 5 trong list vừa nhập, nếu list không có số nào chia hết cho 5 thì hiển thị ra màn hình [0]
Nếu bạn nhập n = 4, lst = [5, 6, 7, 8] thì màn hình sẽ hiển thị ra [5]
Nếu bạn nhập n = 5, lst = [1, 2, 3, 4] thì màn hình sẽ hiển thị ra [0]
Nếu bạn nhập n = 5, lst = [15, 5, 20, 3, 7] thì màn hình sẽ hiển thị ra [15, 5, 20]



'''
n =int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
ans = []
for i in lst:
    if i %5==0:
        ans.append(int(i))

if len(ans)==0:
    ans=[0]
print(ans)