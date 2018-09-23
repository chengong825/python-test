
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 1
        neg = []
        res=nums[0]
        countelse=0
        count0=0

        if len(nums)==1:
            return nums[0]
        nums=[0]+nums+[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i]!=0:
                p *= nums[i]
                countelse+=1
            if nums[i]<0:
                neg.append([p,nums[i]])
            elif nums[i]==0:
                count0+=1
                if p<0:
                    if countelse==0:
                        p=-10000000
                    elif countelse==1:
                        p=p
                    else:
                        p=max(neg[0][0]//neg[0][1],p//(neg[0][0]),neg[-1][0]//neg[-1][1],p//(neg[-1][0]))
                if res<p and nums[i-1]!=0:
                    res=p
                p = 1
                neg = []
                countelse=0
        if count0>1:
            return max(res,0)
        return res


s=Solution()
nums=[0,-1,0]
print(s.maxProduct(nums))