# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
#   [1,3,1],        1,4,5
#   [1,5,1],        2,7,6
#   [4,2,1]         6,8,7
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        min_distance=grid
        m=len(grid)
        n=len(grid[0])
        for i in range(n):
            if i==0:
                min_distance[0][i]=grid[0][i]
            else:
                min_distance[0][i]=min_distance[0][i-1]+grid[0][i]
        for j in range(1,m):
            for i in range(n):
                if i==0:
                    min_distance[j][0] = min_distance[j-1][0] + grid[j][0]
                else:
                    min_distance[j][i]=grid[j][i]+min(min_distance[j-1][i],min_distance[j][i-1])

        return min_distance[m-1][n-1]
solution=Solution()
grid=[[1,3,1],[1,5,1],[4,2,1]]
solution.minPathSum(grid)