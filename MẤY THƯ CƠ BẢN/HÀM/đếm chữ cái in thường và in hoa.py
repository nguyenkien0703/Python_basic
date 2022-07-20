'''cách của mình ,cách của họ in cũng ảo vlon 
'''
# def dem(s):
#     cnt1=0
#     cnt2=0
#     for c in s :
#         if c.isupper():
#             cnt1+=1
#         if c.islower():
#             cnt2+=1
#     print("Given string: " +s)
#     print("Number of uppercase letters: " +str(cnt1))
#     print("Number of lowercase letters: " +str(cnt2))




# s =str(input()) 
# dem(s)


'''cácch cảu họ '''
def show(s):
    count_upper = 0
    count_lower = 0
    for c in s:
        if c.isupper():
            count_upper += 1
        if c.islower():
            count_lower += 1

    print("Given string:",s)
    print("Number of uppercase letters:",count_upper)
    print("Number of lowercase letters:",count_lower)


s = input()
show(s)