class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1=-999
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                max1_=(nums[i]-1)*(nums[j]-1)
                if max1_>max1:
                    max1=max1_
                
            
        return max1
        