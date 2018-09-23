# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 2,9,7,5,3,3,2,1
2,1,2,3,3,5,7,9
3,1,2,2,3,5,7,9
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                end=n-1
                for j in range(i+1,(n+i+1)//2):
                    nums[j],nums[end]=nums[end],nums[j]
                    end-=1
                for j in range(i+1,n):
                    if nums[j]>nums[i]:
                        nums[i],nums[j]=nums[j],nums[i]
                        return

        nums.reverse()

s=Solution()

nums=[2,9,7,5,3,3,2,1]

s.nextPermutation(nums)
print(nums)
