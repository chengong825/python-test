import math
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
m=0
mChange=1
while m<=3:
    n=1
    print(" "*(4-m),end='')
    while n<=2*m+1:
        print("$",end='')
        n=n+1
    print()
    m+=1
while m>=0:
    n = 1
    print(" " * (4 - m), end='')
    while n <= 2 * m + 1:
        print("$", end='')
        n = n + 1
    print()
    m = m-1

while m<=5:
    n=1
    print(" "*(5-m),end='')
    while n<=m:
        print("*",end=' ')
        n=n+1
    print()
    m=m+1