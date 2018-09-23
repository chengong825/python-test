# def f(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         a=1
#         b=1
#         i=2
#         while i<n:
#             c=a
#             a=b
#             b=a+c
#             i=i+1
#         return b
# i=1
# s=0
# while i<1000:
#    s=s+f(i+2)/f(i+1)
#    i+=1
# print(s)
a=2
b=1
s=a/b
i=1
while i<1000:
    c=a
    a=a+b
    b=c
    s=s+a/b
    i=i+1
print(s)