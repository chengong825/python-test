# a=[2,3,3,6,4,48,8,8,4]
# a.append([1,5])
# def fun(a,b,c):
#     return (3*a,3*b,4*c)
# c=fun(2,3,5)
# c=list(c)
# print(c)
# a=2
# b=1
# t=a
# a=b
# b=t
# print(a,b,t)
# temp_list = ["小明","男",172]
# temp_list.append("小白")
# temp_list.remove("小明")
# temp_list[0]="保密"
# print(temp_list[1])
# print(temp_list)
# print(1==1.0)
import re
con="k:1|k1:2|k2:3|k3:4"
dic={}
ls=re.split(r"\|",con)
print(ls)
for x in ls:
    temp_ls=re.split(r":",x)
    print(temp_ls)
    dic[str(temp_ls[0])]=int(temp_ls[1])
print(dic)