''''
Cho chuỗi s được nhập vào từ bàn phím, bạn hãy viết chương trình tạo ra một chuỗi nối 2 kí tự đầu và 2 kí tự cuối của chuỗi s và hiển thị ra màn hình. Nếu chuỗi s có độ dài nhỏ hơn 2 thì hiển thị ra chuỗi rỗng

Nếu bạn nhập s = "Codelearn.io" thì màn hình sẽ hiển thị ra "Coio"
Nếu bạn nhập s = "uno" thì màn hình sẽ hiển thị ra "unno"
Nếu bạn nhập s = "a" thì màn hình sẽ hiển thị ra ""

https://codelearn.io/learning/python-co-ban/40554
'''


s= input()

if len(s) <2 :
    print("")
else :
    print(s[0:2] + s[-2:])
