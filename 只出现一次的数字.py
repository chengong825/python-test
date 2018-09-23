def singleNumber(nums):
    n=len(nums)

    for i in range(n):
        for  j in range(n):
            if nums[j]==nums[i] and j!=i:

                break
        else:
            return nums[i]
num=[1,1,1,3,3,3,2,5,2,2]
print(singleNumber(num))