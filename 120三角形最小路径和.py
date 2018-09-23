
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        deepth=len(triangle)
        for i in range(deepth):
            d=deepth-1-i
            for j in range(d):
                triangle[d-1][j]=triangle[d-1][j]+min(triangle[d][j],triangle[d][j+1])
        return triangle[0][0]

solution=Solution()
triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]
print(solution.minimumTotal(triangle=triangle))