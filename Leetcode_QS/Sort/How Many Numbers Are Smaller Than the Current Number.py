

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        arr=[]
        n=len(nums)
        for i in range(n):
            j =0
            count=0
            while j<=n-1:
                if nums[i]>nums[j]:
                    count = count +1
                j+=1
            arr.append(count)
        return arr
    
sol=Solution()
nums=[8,1,2,2,3]
print(sol.smallerNumbersThanCurrent(nums))