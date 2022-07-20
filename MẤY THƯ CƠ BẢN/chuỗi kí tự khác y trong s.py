# Cho chuỗi s được nhập từ bàn phím, bạn hãy viết chương trình hiển thị ra màn hình các kí tự khác kí tự 'y' trong chuỗi s.
s=input()# mặc định dữ liệu đầu vào là chuỗi nhá 
for c in s:
    if c=='y':
        continue
    print(c)