# 给定一个正整数数组 nums。
#
# 找出该数组内乘积小于 k 的连续的子数组的个数。
#
# 示例 1:
#
# 输入: nums = [10,5,2,6], k = 100
# 输出: 8
# 解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于100的子数组。

# class Solution:
#     def numSubarrayProductLessThanK(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         count=0
#
#         for i in range(len(nums)):
#             p=1
#             for j in range(i,len(nums)):
#                 p*=nums[j]
#                 if p<k:
#                     count+=1
#                 else:
#                     break
#         return count
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        i=0
        j=0
        s=1
        if k<=1:
            return 0
        while j<len(nums):
            if s<k:
                s *= nums[j]
                j+=1
            else:
                s//=nums[i]
                count+=j-i-1
                i+=1
        if s>=k:
            while s>=k and i<len(nums):
                s//=nums[i]
                count+=j-i-1
                i+=1
        return count+(j-i)*(j-i+1)//2


s=Solution()
nums=[3,3,3]
k=2
print(s.numSubarrayProductLessThanK(nums,k))