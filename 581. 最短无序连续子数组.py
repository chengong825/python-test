# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 你找到的子数组应是最短的，请输出它的长度。
#
# 示例 1:
#
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        low = 0
        while low < n - 1 and nums[low] <= nums[low + 1]:
            low += 1
        low += 1

        if low == n:
            return 0
        j = low
        min_val = nums[low]
        while j < n:
            if nums[j] < min_val:
                min_val = nums[j]
            j += 1
        left = 0
        while nums[left] <= min_val:
            left += 1
        high = n - 1
        while high >= 0 and nums[high - 1] <= nums[high]:
            high -= 1
        high -= 1
        max_val = nums[high]
        i = high
        while i >= 0:
            if nums[i] > max_val:
                max_val = nums[i]
            i -= 1
        right = n - 1
        while nums[right] >= max_val:
            right -= 1
        return right - left + 1



s=Solution()
# nums=[1,4,2,3,5]
nums=[2,1]
print(s.findUnsortedSubarray(nums))
