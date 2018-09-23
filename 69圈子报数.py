
# dty={"name":(11,2,2),"sex":25,"interest":"beauty"}
# print(dty["sex"])
# dty["sex"]=[25,12]
# print(dty["sex"])
def fun(k):
    arr=[a for a in range(0,k)]
    i=2
    length=len(arr)
    count=0
    n=length-1
    while count<n:
        while i<length:
            arr.pop(i)
            count+=1
            i-=1
            length=length-1
            i += 3
        i=i%length
    return arr

# def fun(k):
#     arr=[a+1 for a in range(0,k)]
#     length=len(arr)
#     i=2
#     count=0
#     n=length-1
#     while count<n:
#         while i < length:
#             arr.pop(i)
#             length-=1
#             count+=1
#             i+=2
#         i=i%length
#     return arr



for x in range(1,100):
    print("%d个人剩的人"%x,fun(x))