# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#
# 示例 1:
#
# 输入:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出: 3
# 解释:
# 长度最长的公共子数组是 [3, 2, 1]。

# class Solution:
#     def findLength(self, A, B):
#         """
#         :type A: List[int]
#         :type B: List[int]
#         :rtype: int
#         """
#         length=[]
#         for i in range(len(A)):
#
#             count_max=0
#             j=0
#             while j<len(B):
#                 count = 0
#                 while i<len(A) and j<len(B) and A[i]==B[j]:
#                     i+=1
#                     j+=1
#                     count+=1
#
#                 j-=count
#                 i-=count
#                 j+=1
#                 if count>count_max:
#                     count_max=count
#             length.append(count_max)
#
#         return (max(length))

class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        length=[]


        if len(A)>len(B):
            B,A=A,B
        a = len(A) - 1
        for i in range(len(A)):
            count_max = 0
            count=0
            t=0
            for j in range(a-i,len(A)):
                if A[j]==B[t]:
                    count+=1

                else:
                    if count>count_max:
                        count_max=count
                    count=0
                t+=1
            else:
                if count > count_max:
                    count_max = count
            length.append(count_max)
        for i in range(len(B)-len(A)):
            count_max = 0
            count = 0
            t = 0
            for j in range(len(A)):
                if A[t] == B[j+i+1]:
                    count += 1

                else:
                    if count > count_max:
                        count_max = count
                    count = 0
                t+=1
            else:
                if count > count_max:
                    count_max = count
            length.append(count_max)
        for i in range(len(A)-1):
            count_max = 0
            count = 0
            t = 0
            for j in range(len(A)-i-1):
                if A[t] == B[len(B)-(len(A)-i-1)+j]:
                    count += 1
                else:
                    if count > count_max:
                        count_max = count
                    count = 0
                t+=1
            else:
                if count > count_max:
                    count_max = count
            length.append(count_max)
        return max(length)



s=Solution()
A=[1,1,2,3]
B=[1,2,3,1,2,3]
print(s.findLength(A,B))