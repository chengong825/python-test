def get0(n):
    count=0
    while n>0:
        s = n
        while s%5==0:
            count=count+1
            s=s//5
        n=n-1
    return count
print(get0(25))
