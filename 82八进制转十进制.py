n = int(input("请输入一个八进制数："))
s = 0
m = 0
i=0
while n:

    m = n % 10
    s =m*8**i+s
    n = n // 10
    i=i+1
print(s)
