i=101
while 100<=i<=200:
    j=2
    while 1<j<=i//2:
        if i%j==0:
            break
        j=j+1
    if j==i//2+1:
        print(i)
    i=i+1