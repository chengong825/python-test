def f(i,j):
    if i==j or j==1:
        return 1
    else:
        return f(i-1,j-1)+f(i-1,j)
m=1
n=1
while m<=15:
    n=1
    print("   "*(20-m),end='')
    while n<=m:
        print("%5d"%(f(m,n)),end=' ')
        n=n+1
    print()
    m=m+1

# n=1
# while n>0:
#     print(1)