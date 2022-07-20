'''
Cho một list các số nguyên n phần tử lst được nhập từ bàn phím. Bạn hãy viết chương trình hiển thị ra màn hình số nhỏ nhất trong list vừa nhập.

'''
n =int(input())
lst=[];
for i in range(n):
    lst.append(int(input()))
min_val =lst[0]
for i in lst :#duyệt các số trong lst

    if i< min_val:
        min_val =i
print(min_val)
