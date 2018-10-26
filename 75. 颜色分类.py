# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]

class Solution:
    # def sortColors(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     n=len(nums)
    #     i=0
    #     j=0
    #     for k in range(n):
    #         v=nums[k]
    #         nums[k]=2
    #         if v<2:
    #             nums[j]=1
    #             j+=1
    #         if v==0:
    #             nums[i]=0
    #             i+=1

    def sortColors(self, nums):
        red, white, bule = 0, 0, len(nums) - 1
        while white < bule:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[bule] = nums[bule], nums[white]
                bule -= 1


ls = [1, 0, 2, 1, 1, 0]
print(Solution().sortColors(ls))
print(ls)
