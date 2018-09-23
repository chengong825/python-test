def f(n):
    """斐波那契数列"""
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)
#
#
# m = int(input("请输入n："))
# print(f(m))
# def f(n):
#     if n==1:
#         return 1
#     if n==2:
#         return 2
#     i=2
#     a=1
#     b=2
#     while i<n:
#        c=a
#        a=b
#        b=a+c
#        i+=1
#     return b
a=1
b=1
def fib(a,b,n):
    if n>2:
        return fib(a+b,a,n-1)
    return a
print(fib(1,1,5))