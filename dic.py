import copy
dic={}
li=[]
for i in range(10):
    # print(i)
    # if i!=9:
    #     i+=1
    dic['num']=i
    li=copy.deepcopy(li)
    li.append(dic)
print(li)

# print(list)
#
# list=[]
# dic=[1,2,3]
# # list1.append(dic)
# list.append(dic)
# list1=copy.copy(list)
# print(list,list1)
# list1[0][0]=3
# print(list,list1)
# ls=[]
# dic={}
# dic[1]=1
# ls.append(dic)
# ls1=copy.deepcopy(ls)
# dic[1]=2
# ls1.append(dic)
# print(ls,ls1)