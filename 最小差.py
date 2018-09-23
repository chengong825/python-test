#给定数组 A = [3,4,6,7]， B = [2,3,8,9]，返回 0。

# def fun(A,B):
#     na=len(A)
#     nb=len(B)
#     min=abs(A[0]-B[0])
#     for i in range(na):
#         for j in range(nb):
#
#             if min>abs(B[j]-A[i]):
#                 min=abs(B[j]-A[i])
#             if min==0:
#                 return 0
#     return min
# A=[5,5,6,7]
# B=[2,1,10,1]
# x=fun(A,B)
# print(x)
def fun(A,B):
    na=len(A)
    nb=len(B)
    A.sort()
    B.sort()
    minnum=[]
    for i in range(na):
        if B[0] - A[i] > 0:
            curmin = B[0] - A[i]
            minnum.append(curmin)
            continue
        for j in range(nb):
            if B[j]-A[i]==0:
                return 0
            if B[j]-A[i]>0:
                if A[i]-B[j-1]>B[j]-A[i]:
                    curmin=B[j]-A[i]
                    break
                elif A[i]-B[j-1]<B[j]-A[i]:
                    curmin=A[i]-B[j-1]
                    break
        minnum.append(curmin)

    return min(minnum)
A=[24142452]
B=[0]
x=fun(A,B)
print(x)