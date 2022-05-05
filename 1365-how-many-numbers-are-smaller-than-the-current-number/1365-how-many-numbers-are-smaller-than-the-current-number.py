class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list_count=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count=count+1
            list_count.append(count)
        return list_count