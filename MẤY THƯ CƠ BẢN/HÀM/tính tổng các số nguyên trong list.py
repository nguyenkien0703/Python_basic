#Bạn hãy viết hàm trả về tổng của các phần tử trong list các số nguyên được nhập vào từ bàn phím.

def sum_lst(lst):
    ans =0
    for v in lst:
        ans +=v

    return ans




n =int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
print(sum_lst(lst))