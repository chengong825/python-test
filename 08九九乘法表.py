i = 0
j = 0
print(1111)
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d" % (j,i,i*j), end="\t")
        j += 1
    print("")
    i += 1
