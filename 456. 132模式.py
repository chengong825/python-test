# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
#
# 注意：n 的值小于15000。
#
# 示例1:
# 输入: [1, 2, 3, 4]
# 输出: False
# 解释: 序列中不存在132模式的子序列。

# 示例 2:
# 输入: [3, 1, 4, 2]
# 输出: True
# 解释: 序列中有 1 个132模式的子序列： [1, 4, 2].

# 示例 3:
# 输入: [-1, 3, 2, 0]
# 输出: True
# 解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
# class Solution:
#     def find132pattern(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         length = len(nums)
#         if length<3:
#             return False
#         cur=[[nums[0],nums[1]]]
#         curmin=min(nums[0],nums[1])
#         for i in range(2,length):
#             for c in cur:
#                 if c[0]<nums[i]<c[1]:
#                     return True
#                 elif curmin<nums[i]<c[0]:
#                     cur.append([curmin,nums[i]])
#                 elif nums[i]>c[0]:
#                     cur[cur.index(c)]=[curmin,max(nums[i],c[1])]
#                 if nums[i]<curmin:
#                     curmin=nums[i]
#         return False

# class Solution:
#     def find132pattern(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         a=[]
#         for i in range(7500):
#             a.append([0,0])
#         s=0
#         length = len(nums)
#         low=nums[0]
#         high=nums[0]
#         for i in range(1,length):
#             if nums[i]>high:
#                 for j in range(s):
#                     if a[j][0]<nums[i] and nums[i]<a[j][1]:
#                         return True
#                 high=nums[i]
#             elif nums[i]<high:
#                 if high!=low:
#                     a[s][0]=low
#                     a[s][1]=high
#                     s+=1
#                 for j in range(s):
#                     if a[j][0]<nums[i] and nums[i]<a[j][1]:
#                         return True
#                 low=nums[i]
#                 high=nums[i]
#         return False
class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        if n<=2:
            return False
        third=-99999999999
        i=n-1
        second=[]
        while i>=0:
            if nums[i]<third:
                return True
            else:
                while second and second[-1]<nums[i]:
                    third=second.pop()



                second.append(nums[i])
            i-=1
        return False




solution=Solution()
# nums=[3,4,0,1,2]
nums= [ 9,11,8,9,10,7,9]
# nums=[3,5,0,3,4]
print(solution.find132pattern(nums))







# class Solution {
# public:
#     bool find132pattern(vector<int>& nums) {
#         if (nums.size() <= 2) return false;
#         int n = nums.size(), i = 0, j = 0, k = 0;
#         while (i < n) {
#             while (i < n - 1 && nums[i] >= nums[i + 1]) ++i;
#             j = i + 1;
#             while (j < n - 1 && nums[j] <= nums[j + 1]) ++j;
#             k = j + 1;
#             while (k < n) {
#                 if (nums[k] > nums[i] && nums[k] < nums[j]) return true;
#                 ++k;
#             }
#             i = j + 1;
#         }
#         return false;
#     }
# };



# class Solution {
# public:
#     bool find132pattern(vector<int>& nums) {
#         int a[7500][2]={0};  //存放区间
#         int s=0; //已存段数
#         int length=nums.size(); //序列长度
#         if(length==0)
#             return 0;
#         int low=nums[0]; //当前极值
#         int high=nums[0];
#         int i,j;
#         for(i=1;i<length;i++)
#         {
#             if(nums[i]>high)
#             {
#                 for(j=0;j<s;j++)
#                 {
#                     if(nums[i]>a[j][0]&&nums[i]<a[j][1])
#                         return 1;
#                 }
#                 high=nums[i];
#             }
#             else if(nums[i]<high)
#             {
#                 if(high!=low)
#                 {
#                     a[s][0]=low;
#                     a[s][1]=high;
#                     s++;
#                 }
#                 for(j=0;j<s;j++)
#                 {
#                     if(nums[i]>a[j][0]&&nums[i]<a[j][1])
#                         return 1;
#                 }
#                 low=nums[i];
#                 high=nums[i];
#             }
#         }
#         return 0;}
#
# };

