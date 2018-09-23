# 你将获得K个鸡蛋，并可以使用一栋从1到N共有N层楼的建筑。
# 每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
# 你知道存在楼层F ，满足0 <= F <= N
# 任何从高于F的楼层落下的鸡蛋都会碎，从F楼层或比它低的楼层落下的鸡蛋都不会破。
# 每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层X扔下（满足1 <= X <= N）。
# 你的目标是确切地知道F的值是多少。无论F的初始值如何，你确定F的值的最小移动次数是多少？
# 示例1：
# 输入：K = 1, N = 2
# 输出：2
# 解释：
# 鸡蛋从1楼掉落。如果它碎了，我们肯定知道F = 0 。
# 否则，鸡蛋从2楼掉落。如果它碎了，我们肯定知道F = 1 。
# 如果它没碎，那么我们肯定知道F = 2 。因此，在最坏的情况下我们需要移动2次以确定F是多少。
# 示例2：
# 输入：K = 2, N = 6
# 输出：3
# 示例3：
# 输入：K = 3, N = 14
# 输出：4
class Solution:
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        if 2 ** K >= N:
            for i in range(K + 1):
                if 2 ** i == N:
                    return i + 1
                if 2 ** i > N:
                    return i
        # if (N+K) % (2 ** K - 1) == 0:
        #     return ((N+K) // (2 ** K - 1) + K - 2)
        # return ((N+K) // (2 ** K - 1) + K-1)
        old_ls = [2**i for i in range(K)]
        new_ls = [2 ** i for i in range(K)]
        for x in range(1,N+1):
            # if sum(ls)>=N:
            #     return x+K-2
            s=sum(old_ls)+1
            for j in range(K-1,-1,-1):
                if j==K-1:
                    new_ls[j]=s
                if j>0:
                    new_ls[j-1]=new_ls[j]-old_ls[j]
            if sum(new_ls)>=N:
                return new_ls[0]+K-1
            old_ls=new_ls.copy()




solution=Solution()
print(solution.superEggDrop(2,7))