# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
#
# 示例 1 :
#
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。
# 示例 2 :
#
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。

class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_arr=list(map(int,str(num)))
        n=len(num_arr)
        old_vmax=vmax=num_arr[n-1],n-1
        left=-1
        for i in range(n-1,-1,-1):
            if num_arr[i]<vmax[0]:
                left=num_arr[i],i
                old_vmax = vmax
            elif num_arr[i]>vmax[0]:
                vmax=num_arr[i],i
        if left==-1:
            return num
        num_arr[left[1]], num_arr[old_vmax[1]] = num_arr[old_vmax[1]], num_arr[left[1]]
        return int(''.join(map(str,num_arr)))
s=Solution()
# nums=
print(s.maximumSwap(123456))