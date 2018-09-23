n=int(input("请输入四位数字"))
s=0
while n:
    m=n%10
    m=(m+5)%10
    s=s*10+m
    n=n//10
print(s)