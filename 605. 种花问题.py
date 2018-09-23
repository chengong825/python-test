# 假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
#
# 给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。
#
# 示例 1:
#
# 输入: flowerbed = [1,0,0,0,1], n = 1
# 输出: True
# 示例 2:
#
# 输入: flowerbed = [1,0,0,0,1], n = 2
# 输出: False

# class Solution:
#     def canPlaceFlowers(self, flowerbed, n):
#         """
#         :type flowerbed: List[int]
#         :type n: int
#         :rtype: bool
#         """
#         length=len(flowerbed)
#         count1=0
#         count0=0
#         first=0
#         if flowerbed[first]==0:
#             while first<length and flowerbed[first]==0:
#                 first+=1
#         last=length-1
#         if flowerbed[last]==0:
#             while last>=0 and flowerbed[last]==0:
#                 last-=1
#         if first==length:
#             count1= (length+1)//2
#         else:
#             i=first+1
#             while i<=last:
#                 while flowerbed[i]==0:
#                     count0+=1
#                     i+=1
#
#                 count1+=(count0+1)//2-1
#                 count0=0
#                 i += 1
#             count1= first//2+count1+(length-1-last)//2
#         if count1>=n:
#             return True
#         return False

# class Solution:
#     def canPlaceFlowers(self, flowerbed, n):
#         """
#         :type flowerbed: List[int]
#         :type n: int
#         :rtype: bool
#         """
#         i=0
#         count=0
#         j=0
#         while i<len(flowerbed):
#             if flowerbed[i]==0:
#                 j=i
#                 while j<len(flowerbed) and flowerbed[j]==0:
#                     j+=1
#                 if i==0 and j==len(flowerbed):
#                     count+=(j+1)//2
#                 elif i==0 or j==len(flowerbed):
#                     count+=(j-i)//2
#                 else:
#                     count+=(j-i+1)//2-1
#                 i=j
#             i+=1
#         if count>=n:
#             return True
#         return False
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        zero=1
        po=0
        for i in flowerbed:
            if i==1:
                po+=(zero-1)/2
                zero=0
            else:
                zero+=1
        if zero>1:
            po+=zero/2
        return po>=n
s=Solution()
print(s.canPlaceFlowers([0,1,0,0,0,1],2))


# class Solution {
# public:
#     bool canPlaceFlowers(vector<int>& flowerbed, int n) {
#         int i,count=0;
#         int j=0;
#         while(i<flowerbed.size())
#         {
#             if(flowerbed[i]==0)
#             {
#                 for(j=i;j<flowerbed.size()&&flowerbed[j]==0;j++);
#                 if(i==0&&j==flowerbed.size())
#                     count+=(j+1)/2;
#                 else if(i==0||j==flowerbed.size())
#                     count+=(j-i)/2;
#                 else
#                     count+=(j-i+1)/2-1;
#                 i=j;
#             }
#             i++;
#         }
#         if(count>=n) return 1;
#         return 0;
#     }
# };