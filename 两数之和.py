
def twosum(numbers,target):
    d = {}
    num_list=[]
    for i in range(len(numbers)):
        a = target - numbers[i]
        if numbers[i] in d:
            print(d[numbers[i]]+1, i+1)
            num_list.append([d[numbers[i]]+1, i+1])
        else:
            d[a] = i
        print(d)
    return num_list
# def twosum(nums,target):
#
#     num_list = [[]]
#     for num1 in nums:
#         num2 = target - num1
#         if num2 in nums and num1 != num2:
#             sum = [num1, num2]
#             sum.sort()
#             for i in num_list:
#                 if i == sum:
#                     break
#             else:
#                 num_list.append(sum)
#
#     num_list.pop(0)
#     print(num_list)
nums = [3,3]
target = 6
f=twosum(nums,target)
print(f)
