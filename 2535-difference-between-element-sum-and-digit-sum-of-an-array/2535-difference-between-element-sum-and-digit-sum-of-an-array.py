class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        new=[]
        nums1=list(map(str,nums))
        for i in range(len(nums1)):
            for j in nums1[i]:
                new.append(int(j))
        
        return sum(nums)-sum(new)