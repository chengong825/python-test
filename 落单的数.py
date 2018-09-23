# a=[{1:1,2:3},{1:1,2:2},{1:1,2:4}]
# print(a.count({1:1}))

# def swap(a,b):
#     t=a
#     a=b
#     b=t
#     print(a,b)
# c=2
# d=1
# swap(c,d)
# print(c,d)

class solution():
    def singleNum(self,a):
        sum=0
        for y in a:
            sum+=y
        b=set(a)
        c=list(b)
        s=0
        for x in c:
           s+=x
        print(c)
        return 2*s-sum
d=[1,1,2,2,3,4,4,5,5]
m=solution()

print(m.singleNum(d))