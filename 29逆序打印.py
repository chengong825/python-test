n=int(input("请输入5位以内的整数"))
N=n
s=0
i=0
while n:

    m = n % 10
    n = n // 10
    s=s*10+m
    i=i+1
    print(m)
print("%d位数%d"%(i,s))
if s==N:
    print("yes")
else:
    print("no")
