count = 0
i = 1
while 1 <= i <= 4:
    j = 1
    while 1 <= j <= 4:
        if j != i:
            k = 1
            while 1 <= k <= 4:
                if k != j and k != i:
                    print("%d%d%d" % (i, j, k))
                    count = count + 1
                k = k + 1
        j = j + 1
    i = i + 1
print(count)
