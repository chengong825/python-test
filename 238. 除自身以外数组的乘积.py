# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
# 其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
# 示例:
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # n=len(nums)
        # left = [0]*n
        # right = [0]*n
        # left[0]=nums[0]
        # right[n-1]=nums[n-1]
        # for i in range(1,n):
        #     left[i]=left[i-1]*nums[i]
        #     right[n-1-i]=right[n-i]*nums[n-1-i]
        #
        # res=[right[1]]
        # for i in range(1,n-1):
        #     res.append(left[i-1]*right[i+1])
        # res.append(left[n-2])
        # return res
        p = 1
        n = len(nums)
        output = []
        for i in range(0, n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
s=Solution()
nums=[1,2,3,4]
print(s.productExceptSelf(nums))