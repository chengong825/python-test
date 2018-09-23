s = int(input("请输入一个大于或等于2的正整数："))
i = 2
n = s
print(n, "= ", end="")
# while i <= n:
#     j = 2
#     while 2 <= j <= i // 2:  # 判断i是否为素数
#         if i % j == 0:
#             break
#         j = j + 1
#     if j == i // 2 + 1:  # i是素数
#         if i == s:
#             print("素数,无法分解质因数")
#         else:
#             while n % i == 0:
#                 print(i, end="")
#                 if i != n:
#                     print(" * ", end='')
#                 n = n // i
#
#     i = i + 1
while i <= n//2:
    j = 2
    while 2 <= j <= i // 2:  # 判断i是否为素数
        if i % j == 0:
            break
        j = j + 1
    if j == i // 2 + 1:  # i是素数

        while n % i == 0:
            print(i, end="")
            if i != n:
                print(" * ", end='')
            n=n//i
    i = i + 1
if n==s:
    print("素数,无法分解质因数")
elif n!=1:
    print(n)