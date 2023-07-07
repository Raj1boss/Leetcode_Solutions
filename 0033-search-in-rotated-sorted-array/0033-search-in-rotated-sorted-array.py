class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count=0
        for i in range(len(nums)):
            if target in nums:
                index_v=nums.index(target)
                return index_v
            else:
                return -1
                
                
                

                
        