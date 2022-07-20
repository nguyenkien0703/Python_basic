# Cho số nguyên n được nhập vào từ bàn phím, bạn hãy viết chương trình hiển thị ra tổng của dãy số 1/2 + 2/3 + ... + n/n+1.
#Lưu ý: chỉ hiển thị 2 chữ số thập phân sau dấu phẩy.
n= int(input())
ans =0
for i in range(1,n+1):
    ans +=i/(i+1);
print(round(ans,2))



