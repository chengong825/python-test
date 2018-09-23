n=1
s=0
sum=0
i=n%10
count=0
while count<20:
    total = 0
    while n:
        j = 0
        while i==n%10:
            j+=1
            n//=10
        s=j*10+i
        while sum:
            sum//=10
            s*=10
        total+=s
        sum=s
        i=n%10
    print(total)
    n=total
    count+=1