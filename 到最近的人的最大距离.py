# 在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
#
# 至少有一个空座位，且至少有一人坐在座位上。
#
# 亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
#
# 返回他到离他最近的人的最大距离。
# 输入：[1,0,0,0,1,0,1]
# 输出：2
# 解释：
# 如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
# 如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
# 因此，他到离他最近的人的最大距离是 2 。
seats=[1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0]
# n=len(seats)
# minlen=[]
# for i in range(n):
#     if seats[i]==0:
#         j=1
#         while i+j<n:
#             if seats[i+j]==1:
#                 break
#             j+=1
#         k=1
#         while i-k>=0:
#             if seats[i-k]==1:
#                 break
#             k+=1
#         if i+j==n:
#             r=k
#         elif i-k==-1:
#             r=j
#         else:
#             r=min(j,k)
#         minlen.append(r)
# print(max(minlen))

def get_stu_pos(seats):
    return [x for x in range(len(seats)) if seats[x] == 1]
def get_stu_dis(l):
    return [l[i + 1] - l[i] for i in range(len(l) - 1)]
def maxDistToClosest(seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    l =get_stu_pos(seats)
    print(l)
    distance=get_stu_dis(l)
    print(distance)
    maxm = max(distance + [0]) // 2
    if seats[0] == 0:
        maxm = max(maxm, l[0])
    if seats[-1] == 0:
        maxm = max(maxm, len(seats) - 1 - l[-1])
    return maxm
print(maxDistToClosest(seats))
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n=len(seats)
        minlen=[]
        for i in range(n):
            if seats[i]==0:
                j=1
                while i+j<n:
                    if seats[i+j]==1:
                        break
                    j+=1
                k=1
                while i-k>=0:
                    if seats[i-k]==1:
                        break
                    k+=1
                if i+j==n:
                    r=k
                elif i-k==-1:
                    r=j
                else:
                    r=min(j,k)
                minlen.append(r)
        return max(minlen)
