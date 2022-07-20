def show(s):
    chieudai=len(s)
    if chieudai  <= 3:
        print(s)
    else:
        ans=s[-3:]
        if ans == "ing":
            s+="ly"
        else:
            s+="ing"
        print(s)


s=input()

show(s)





