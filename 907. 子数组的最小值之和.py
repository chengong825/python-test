# 给定一个整数数组A，找到min(B)的总和，
# 其中B的范围为A的每个（连续）子数组。
# 由于答案可能很大，因此返回答案模10 ^ 9 + 7。
#
# 示例：
# 输入：[3, 1, 2, 4]
# 输出：17
# 解释：
# 子数组为[3]，[1]，[2]，[4]，[3, 1]，[1, 2]，[2, 4]，[3, 1, 2]，[1, 2, 4]，[3, 1, 2, 4]。
# 最小值为3，1，2，4，1，1，2，1，1，1，
# 和为17。
# class Solution:
#     def sumSubarrayMins(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         n=len(A)
#         res=A
#         total=0
#         for i in range(n):
#             temp = res[0]
#             sums=res[0]
#             for j in range(1,n-i):
#                 a = temp
#                 sums+=res[j]
#                 temp=res[j]
#                 res[j-1]=(a if a<res[j] else res[j])
#             total+=sums
#             print(total)
# #         return total%1000000007
# class Solution:
#     def sumSubarrayMins(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         n=len(A)
#         res=0
#         for i in range(n):
#             r=1
#             l=1
#             while i+r<n and A[i]<=A[i+r] :
#                 r+=1
#             while i-l>=0 and A[i]<A[i-l] :
#                 l+=1
#             count=l*r
#             res+=count*A[i]
#         return res%1000000007
# class Solution:
#     def sumSubarrayMins(self, A):
#         res = 0
#         stack = []  # increasing
#         A = [float('-inf')] + A + [float('-inf')]
#         for i, n in enumerate(A):
#             while stack and A[stack[-1]] > n:
#                 cur = stack.pop()
#                 res += A[cur] * (i - cur) * (cur - stack[-1])
#             stack.append(i)
#         return res % (10**9 + 7)

class Solution:
    def sumSubarrayMins(self, A):
        res = 0
        stack = []  # increasing
        A=[float('-inf')]+A+[float('-inf')]
        for i,n in enumerate(A):
            while stack and A[stack[-1]]>n:
                cur=stack.pop()
                res += A[cur] * (i - cur) * (cur - stack[-1])
            stack.append(i)
        return res%(10**9 + 7)
s=Solution()
print(s.sumSubarrayMins([3,1,2,4]))