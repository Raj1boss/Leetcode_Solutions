class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        list_new=[]
        for i in range(0,len(nums),2):
            fre,val=nums[i],nums[i+1]
            for j in range(fre):
                list_new.append(val)
        return list_new