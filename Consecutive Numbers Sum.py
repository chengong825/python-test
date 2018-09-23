def fun(n):
    j=1
    count=1
    while j<=n//2+1:
        sum_num=0
        for i in range(j,n//2+2):
            sum_num+=i
            if sum_num==n:
                count+=1
                break
            elif sum_num>n:
                break
        j+=1

    return count

print(fun(16))
# def fun(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         j=1
#         count=1
#         sum_num = 0
#         t=j
#         while j<=n//2+1:
#             for x in range(t,n//2+2):
#                 sum_num+=x
#                 if sum_num==n:
#                     count+=1
#                     sum_num -= j
#                     t = x+1
#                     break
#                 elif sum_num>n:
#                     sum_num-=x
#                     sum_num-=j
#                     t=x
#                     break
#                 print(sum_num)
#             j+=1
#         return count
print(fun(4))