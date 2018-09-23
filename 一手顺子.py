# 爱丽丝有一手（hand）由整数数组给定的牌。
#
# 现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。
#
# 如果她可以完成分组就返回 true，否则返回 false。
# 输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
# 输出：true
# 解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
# import unittest
# class NamesTestCase(unittest.TestCase):
#     pass
hand = [1, 5, 2, 3, 4, 4, 6, 7, 8,9,10,11]
print(hand)
W=4
hand.sort()

def fun(hand,W):
    n=len(hand)
    if n%W==0:

        count=0
        cur=hand[0]
        while len(hand):
            if cur+count in hand:
                hand.remove(cur+count)
                count+=1
                if count==W:
                    count=0
                    if len(hand):
                        cur=hand[0]
            else:
                return False
        if count==0:
            return True
        else:
            return False
    else:
        return False
print(fun(hand,W))
