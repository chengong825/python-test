def goodnum(n):
    count=0
    for x in range(1,n+1):
        good = 0
        while x:


            i=x%10
            if i==3 or i==4 or i==7:
                break
            if i==2 or i==5 or i==6 or i==9:
                good=1
            x//=10
        if x==0 and good==1:
            count+=1
    return count
print(goodnum)

