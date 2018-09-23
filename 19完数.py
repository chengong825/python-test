n=1
while n<1000:
    i = 2
    sum=1
    while i<=n//2:
        if n%i==0:
            sum+=i
        i+=1
    if n==sum:
        print(n,"是完数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    n=n+1
