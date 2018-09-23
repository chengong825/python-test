def sum(num):
    while 1:
        s = 0
        while num:
            i = num % 10
            s += i
            num //= 10
        num = s
        if num < 10:
            return num


print(sum(38))
