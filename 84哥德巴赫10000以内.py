n = 4
count = 0
while n <= 10000:
    i = 2
    while i < n:
        j = 2
        while 1 < j <= i // 2:
            if i % j == 0:
                break
            j = j + 1
        if j == i // 2 + 1:
            m = n - i
            j = 2
            while 1 < j <= m // 2:
                if m % j == 0:
                    break
                j = j + 1
            if j == m // 2 + 1:
                print("%d可以表示成%d和%d的和" % (n, i, m))
                count = count + 1
                break
        i = i + 1
    n = n + 2
print(count)
