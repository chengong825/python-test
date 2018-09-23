def judgeSquareSum(n):
    for i in range(n+1):
        for j in range(n+1):
            if i*i+j*j==n:
                # print("%d+%d=%d"%(i*i,j*j,n))
                return True
            if i*i+j*j>n:
                break
    else:
        return False
for x in range(0,101):
    print(x,judgeSquareSum(x))
