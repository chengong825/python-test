# 如果数组是单调递增或单调递减的，那么它是单调的。
# 如果对于所有i <= j，A[i] <= A[j]，那么数组A是单调递增的。
# 如果对于所有i <= j，A[i] > = A[j]，那么数组
# A是单调递减的。
# 当给定的数组A是单调数组时返回true，否则返回 false。
#
# 示例1：
# 输入：[1, 2, 2, 3]
# 输出：true
#
# 示例2：
# 输入：[6, 5, 4, 4]
# 输出：true
#
# 示例3：
# 输入：[1, 1, 1]
# 输出：true
# class Solution:
#     def isMonotonic(self, A):
#         """
#         :type A: List[int]
#         :rtype: bool
#         """
#         length = len(A)
#         for i in range(1, length):
#             if A[i] > A[i - 1]:
#                 for j in range(i + 1, length):
#                     if A[j] < A[j - 1]:
#                         return False
#                 else:
#                     return True
#             elif A[i] < A[i - 1]:
#                 for j in range(i + 1, length):
#                     if A[j] > A[j - 1]:
#                         return False
#                 else:
#                     return True
#         else:
#             return True

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        f1 = False
        f2 = False
        for i in range(len(A)-1):
            if A[i]> A[i+1]:
                f1 = True
            if A[i] < A[i+1]:
                f2 = True
        if f1 and f2:
            return False
        return True
solution=Solution()
A=[1,3,5,4,7]
print(solution.isMonotonic(A))