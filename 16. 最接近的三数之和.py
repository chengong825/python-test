# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # nums.sort()
        # n = len(nums)
        # res = []
        # dif_min=[float('inf'),0]
        # for i in range(n - 2):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #
        #     left, right = i + 1, n - 1
        #     while left < right:
        #         if nums[left] + nums[right] == target - nums[i]:
        #             res.append([nums[i], nums[left], nums[right]])
        #             left += 1
        #             while left < right and nums[left] == nums[left - 1]:
        #                 left += 1
        #         elif nums[left] + nums[right] < target - nums[i]:
        #             dif = target - nums[i] - nums[left] - nums[right]
        #             left += 1
        #             if dif<dif_min[0]:
        #                 dif_min=[dif,target-dif]
        #
        #         else:
        #             dif = nums[left] + nums[right] +nums[i] - target
        #             right -= 1
        #             if dif<dif_min[0]:
        #                 dif_min=[dif,dif+target]
        # return dif_min[1]
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                if nums[left] + nums[right] == target - nums[i]:
                    return target
                elif nums[left] + nums[right] < target - nums[i]:
                    dif = target - nums[i] - nums[left] - nums[right]

                    if dif < abs(res - target):
                        res = nums[i] + nums[left] + nums[right]
                    left += 1
                else:
                    dif = nums[left] + nums[right] + nums[i] - target

                    if dif < abs(res - target):
                        res = nums[i] + nums[left] + nums[right]
                    right -= 1
        return res

s = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(s.threeSumClosest(nums, target))
