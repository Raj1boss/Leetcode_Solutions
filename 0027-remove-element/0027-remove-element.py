class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        co=nums.count(val)
        for i in range(co):
            if val in nums:
                nums.remove(val)
        return len(nums)
        