
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# class Solution:
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         n=len(nums)
#         for i in range(n):
#             if nums[i]==0:
#                 for j in range(i+1,n):
#                     if nums[j]!=0:
#                         nums[i],nums[j]=nums[j],nums[i]
#                         # break
class Solution:
    def moveZeroes(self, nums):
        i=0
        j=0
        while i<len(nums):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]     # 两个变量数值交换
                j+=1
                i+=1
            else:
                i+=1

s=Solution()
nums=[0,1,1,1]
print(s.moveZeroes(nums),nums)