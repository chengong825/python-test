# 给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。
#
# 求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。
#
# 例如 :
# 输入:
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# 输出: 3
# 解释: 满足条件的子数组: [2], [2, 1], [3].

class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """

        res = 0
        # A = [float('inf')]+A+[float('inf')]
        stack=[]
        for i, n in enumerate(A):

            while stack and A[stack[-1]] < n:
                cur = stack.pop()
                if L<=A[cur]<=R:
                    res += (i - cur) * (cur - stack[-1])

            stack.append(i)
        return res
        # res = 0
        # start = end = -1  # 一个合适的开始位置
        # for i in range(len(A)):
        #     if A[i] > R:
        #         start = end = i
        #     # 此时双指针不动，驻足观察情况，看后面是否会有在区间内的数字出现
        #     elif A[i] < L:  # 小于L的数字可以被纳入子数组中，但是不能作为开头
        #         res += end - start
        #     # 介于L和R之间的数字，既可以作为开头，也可以被纳入子数组；已有的子数组中以每个元素开头至此元素结束都可以作为一个新的符合要求的子数组
        #     else:
        #         res += i - start
        #         end = i
        # return res


s=Solution()
print(s.numSubarrayBoundedMax([2,1,4,3],2,3))