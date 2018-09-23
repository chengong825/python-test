arr=[-2,2,-3,4,-1,2,1,-5,3]

i=0
length=len(arr)
b=[]
s=0
while i<length:
    s+=arr[i]
    b.append(s)
    i+=1

print(b)
j=0
if b[j]>0:
    minsum=0
else:
    minsum=b[j]
maxsum=b[j]
while j<length-1:
    j+=1
    if minsum>b[j]:
        minsum=b[j]
    if b[j]-minsum>maxsum:
        maxsum=b[j]-minsum
print(minsum,maxsum)

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        max_sum=nums[0]
        for i in nums:
            x+=i
            if max_sum<x:
                max_sum=x
            if x<0:
                x=0
        return max_sum

s=Solution()
print(s.maxSubArray(arr))