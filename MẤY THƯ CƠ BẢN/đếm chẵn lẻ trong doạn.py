a=int(input())
b=int(input())
cn1,cnt2=0,0
for i in range(a,b+1):
    if i%2==0:
        cn1+=1
    else: cnt2+=1


print(cn1,cnt2)