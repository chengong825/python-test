# 8614912000000
# 8614912499999

# def get_com(start,end):
#     com=''
#     res=[]
#     n=len(start)
#
#     for i in range(n):
#         if start[i]==end[i]:
#             com+=start[i]
#         else:
#             temp_com=com
#             for j in range(i,n):
#                 flag=int(start[j])
#                 count = n - j
#                 while flag<=9:
#
#                     num=temp_com+'0'*count
#                     if num>=start:
#                         for k in range(1,10):
#                             num=temp_com+str(k)+'0'*(count-1)
#                             if num>end:
#                                 if flag==9:
#                                     flag+=1
#                                     break
#                                 temp_com+=start[j]
#                                 break
#                         else:
#                             print(temp_com)
#                             res.append(temp_com)
#                             flag+=1
#                             if flag>9:
#                                 break
#                             temp_com=temp_com[:-1]+str(flag)
#                     else:
#                         temp_com+=start[j]
#                         count-=1
#
#     return res
def get_com(start, end):
    com = ''
    res = []
    n = len(start)
    for i in range(n):
        if start[i] == end[i]:
            com += start[i]
        else:
            temp_com = com
            j = i

            while temp_com + '0' * (n - j) <= end and j < n:

                for k in range(10):
                    num1 = temp_com + str(k) + '0' * (n - j - 1)
                    num2 = temp_com + str(k) + '9' * (n - j - 1)
                    if num1 < start or num2 > end:
                        temp_com += start[j]
                        j += 1
                        break
                else:
                    res.append(temp_com)
                    temp_com = int(temp_com)
                    temp_com += 1
                    temp_com = str(temp_com)
                    m=1
                    if temp_com[-1]=='0':
                        while temp_com[-m]=='0':
                            m+=1
                        temp_com=temp_com[:-m+1]
                        j-=m-1

    return res


print(get_com('8614912500000', '8614919519999'))
