class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max(nums)
        min1 = min(nums)
        nums.pop(nums.index(max1))
        nums.pop(nums.index(min1))
        max2 = max(nums)
        min2 = min(nums)

        return (max1*max2)-(min1*min2)