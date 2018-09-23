# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
#
# 示例 1:
#
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 示例 2:
#
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 1
        if n==3:
            return 2
        product=1
        while n>4:
            product*=3
            n-=3
        return  n*product

solution=Solution()
solution.integerBreak(32)
#3=1+2 4=2+2  6=3+3 11 4 4 3*3*3*3  16 3*3*3*3*3*3*1