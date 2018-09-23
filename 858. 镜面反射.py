# 有一个特殊的正方形房间，每面墙上都有一面镜子。除西南角以外，每个角落都放有一个接受器，编号为
# 0， 1，以及2。
# 正方形房间的墙壁长度为 p，
# 一束激光从西南角射出，首先会与东墙相遇，入射点到接收器0的距离为q 。
# 返回光线最先遇到的接收器的编号（保证光线最终会遇到一个接收器）。

# 示例：
# 输入： p = 2, q = 1
# 输出： 2
# 解释： 这条光线在第一次被反射回左边的墙时就遇到了接收器 2 。
class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        while p%2==0 and q%2==0:
            p//=2
            q//=2
        if p%2==0:
            return 2
        elif q%2==0:
            return 0
        else:
            return 1