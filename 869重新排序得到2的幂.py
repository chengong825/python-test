# 从正整数 N 开始，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
#
# 如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
# 示例 1：
# 输入：1
# 输出：true

# 示例 2：
# 输入：10
# 输出：false

# 示例 3：
# 输入：16
# 输出：true

# 示例 4：
# 输入：24
# 输出：false

# 示例 5：
# 输入：46
# 输出：true
class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        ls=[]
        for i in str(N):
            ls.append(int(i))
        length=len(ls)
        for i in range(length):

solution=Solution()
solution.reorderedPowerOf2(23)