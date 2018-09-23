# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
# 找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# nums =  [-9,1,-6,-4,-4,0,-1,2,-6,5,6,-9,-10,-8,0,9,-6,4,-8,6,4,1,-10,-1,-9,-9,5,-4]
# i = 1
# a=1
# null_list = [[]]
# for num1 in range(0, len(nums) - 2):
#
#     for num2 in range(i, len(nums) - 1):
#         a  += 1
#         for num3 in range(a, len(nums)):
#             print([num1, num2, num3])
#             #         if nums[num1] + nums[num2] + nums[num3] == 0:
#             #             list = [nums[num1], nums[num2], nums[num3]]
#             #             list.sort()
#             #             print(list)
#             #             for b in null_list:
#             #
#             #                 if list == b:
#             #                     break
#             #             else:
#             #
#             #                 null_list.append(list)
#
#         a += 1
#
#     i += 1
#
# null_list.remove([])
# print(null_list)
# i=0
# length=len(nums)
# a=[]
# while i<length:
#     j=i+1
#     while j<length:
#         k=j+1
#         while k<length:
#
#             if nums[i]+nums[j]+nums[k]==0:
#                 b=[nums[i],nums[j],nums[k]]
#                 b.sort()
#                 a.append(b)
#                 # print(a)
#             k+=1
#         j+=1
#     i+=1
# c=[]
# for x in a:
#     while x not in c:
#         c.append(x)
# print(c)
# i=0
# nums.sort()
# length=len(nums)
# a=[]
# print(nums)
# while i<length:
#     j=0
#     k=length-1
#     while j<k:
#         if j==i:
#             j+=1
#         elif k==i:
#             k-=1
#         else:
#             if nums[i]+nums[j]+nums[k]==0:
#                 b = [nums[i], nums[j], nums[k]]
#                 b.sort()
#                 a.append(b)
#                 j+=1
#                 k-=1
#             elif nums[j]+nums[k]<-nums[i]:
#                 j+=1
#             else:
#                 k-=1
#     i+=1
# c=[]
# for x in a:
#     while x not in c:
#         c.append(x)
# print(c)
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            left,right=i+1,n-1
            while left<right:
                if nums[left]+nums[right]==target:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    right-=1
        return res
s=Solution()
nums=[-1,0,1,2,-1,-4]
print(s.threeSum(nums))