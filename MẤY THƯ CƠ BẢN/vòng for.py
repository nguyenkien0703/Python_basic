#tính tổng  các số từ  1 đến n 
#cách 1 : dùng while
# dữ liệu nhâọp vào mặc định là 1 chuỗi nên ta phải ép kiêu rnó về dạng int 



n = int(input()) 
# ans =0 
# i=1 
# while  i<=n :
#     ans +=i
#     i+=1
# print(ans)
'''

Không giống với vòng lặp while, vòng lặp for được dùng để lặp qua một tập hợp cho trước, vòng lặp for thường được sử dụng với hàm range(). Ví dụ:

for i in range(1, 5):
    print(i)
Kết quả khi chạy chương trình:

1 2 3 4 
Giải thích: range() chính là hàm trả về một tập hợp, như ở ví dụ trên thì range(1, 5) sẽ trả về một tập hợp chứa các số từ 1 tới 4.
Ngoài ra, bạn có thể sử dụng vòng lặp for để duyệt qua các ký tự của một xâu. Ví dụ:
name = "Codelearn"
for c in name:
    print(c)
sau khi chạy : C
o
d
e
l
e
a
r
n

'''

'''cách 2 : dùng vòng for'''
ans =0 
for i in range(1,n+1): 
    ans +=i;
print(ans)