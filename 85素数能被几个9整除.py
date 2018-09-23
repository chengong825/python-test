i=7

while i<=100:
    j=2
    while 1<j<=i//2:
        if i%j==0:
            break
        j=j+1
    if j==i//2+1:
        print(i,end=' ')
        k = 9
        while k%i!=0:
            k=k*10+9
        print(k)
    else:
        print(i,"不是素数")
    i=i+1