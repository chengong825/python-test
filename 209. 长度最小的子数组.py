
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#
# 示例:
#
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sums = 0
        j = 0
        res = 999999999

        for i in range(len(nums)):

            if nums[i] >= s:
                return 1
            sums += nums[i]
            while sums >= s:
                sums -= nums[j]
                j += 1
            if sums + nums[j - 1] >= s:
                lmin = i - j + 2
                if lmin < res:
                    res = lmin
        return res

s=Solution()
k=5
nums=[2,3,1,1,1,1,1]
print(s.minSubArrayLen(k,nums))