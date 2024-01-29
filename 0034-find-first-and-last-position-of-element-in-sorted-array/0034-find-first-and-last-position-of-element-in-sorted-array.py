class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            first=nums.index(target)
            second=len(nums)-1-nums[::-1].index(target)
            return [first,second]
        else:
            return [-1,-1]