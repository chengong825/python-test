# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
#
# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
#
# 示例 1:
#
# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释:
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
# 示例 2:
#
# 输入: [1,2,2,3,1,4,2]
# 输出: 6

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}

        for i in range(len(nums)):
            if not d.get(nums[i]):
                d[nums[i]]=[i,i,1]
            else:
                d[nums[i]][2] =  d.get(nums[i])[2]+1
                d[nums[i]][1]=i
        d={i:[j[1]-j[0]+1,j[2]] for i,j in d.items()}
        res=list(d.values())
        print(res)
        res=sorted(res,key=lambda x:(-x[1],x[0]))
        print(res)
        return res[0][0]
s=Solution()
nums=[1,2,2,3,1]
print(s.findShortestSubArray(nums))