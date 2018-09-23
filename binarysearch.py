# def remove_list(what_list,cla):
#
#     i = 1
#     a = 0
#     lenght = len(what_list)
#     while i <= lenght:
#         if what_list[a] == cla:
#             what_list.remove(cla)
#             a -= 1
#         i += 1
#         a += 1
# def fun(list,num):
#     i=0
#     while i<len(list):
#         if list[i]==num:
#             return True
#         i+=1
#     return False
# def fun2(list1,num):
#     i=0
#     while i<len(list1):
#         if fun(list1,num)==True:
#             list1.remove(num)
#             i-=1
#         i+=1

# def fun3(arr,n):   #  a把x001 给了 arr
#     length=len(arr)
#     i=0
#     b=[]
#     while i<length:
#         if arr[i]!=n:
#             b.append(a[i])
#         i+=1
#     arr=b    # arr 把
#     print(arr)
#     return arr
# a=[1,2,4,4,4,5,6,3,7,8]  # a有一个钥匙 可以 打开 [1,2,4,4,4,5,6,3,7,8]  x001
# a=fun3(a,4)




# def func(a, b=[]):  # b的默认值指向一个空的列表，每次不带默认值都会指向这块内存
#     b.append(a)
#     return b
#
#
# print(func(1))  # 向默认的空列表里加入元素1 ，默认列表里已经是[1]
# print(func(2))  # 向默认的列表里加入元素2,默认列表里已经是[1,2]
#
# print(func(3, []))  # 向b指向的空列表里加入元素1 ，默认列表里还是[1,2]
# print(func(4))  # 向默认的列表里加入元素4,默认列表里已经是[1,2,4]
# a="  asda\nsc"
# print(a.)
def fun(a,target):
    length=len(a)
    pl=0
    pr=length-1
    while pl<=pr:
        pt=(pl+pr)//2
        if a[pt]>target:
            pr=pt-1
        elif a[pt]<target:
            pl=pt+1
        else:
            return pt
    return None
a='asdasd'
print(str(list(a)))


