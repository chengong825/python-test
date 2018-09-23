# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {0:1} # prefix sum array
        res = pre_sum = 0
        sums.get(0)
        for n in nums:
            pre_sum += n # increment current sum
            res += sums.get(pre_sum - k, 0) # check if there is a prefix subarray we can take out to reach k
            sums[pre_sum] = sums.get(s, 0) + 1 # add current sum to sum count
        return res




s=Solution()
nums=[1,1,1]
print(s.subarraySum(nums,2))