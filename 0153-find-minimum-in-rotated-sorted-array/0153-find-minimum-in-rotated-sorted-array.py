class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_arr=nums[0]
        for i in range(len(nums)):
            if nums[i]<min_arr:
                min_arr=nums[i]
        return min_arr
        