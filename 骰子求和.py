# 扔 n 个骰子，向上面的数字之和为 S。给定 Given n，请列出所有可能的 S 值及其相应的概率。
# 样例
# 给定 n = 1，返回 [ [1, 0.17], [2, 0.17], [3, 0.17], [4, 0.17], [5, 0.17], [6, 0.17]]。
class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        cur_res = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
        for i in range(2, n + 1):
            new_res = {}
            for k in range(i, i * 6 + 1):
                new_res[k] = cur_res.get(k - 1, 0) + cur_res.get(k - 2, 0) + cur_res.get(k - 3, 0) + cur_res.get(k - 4,
                                                                                                                 0) + cur_res.get(
                    k - 5,
                    0) + cur_res.get(
                    k - 6, 0)
            cur_res = new_res
        probability = []
        for k, v in cur_res.items():
            probability.append([k, v / (6 ** n)])
        return probability


s = Solution()

print(s.dicesSum(3))


