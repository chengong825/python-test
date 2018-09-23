def f(n):
    if n==1 or n==0:
        return 1
    else:
        return f(n-1)*n

i=1
s=0
while i<=20:
    s=s+f(i)
    i=i+1
print(s)