class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        f=[]
        first=nums[:n]
        seond=nums[n:]
        for i in range(len(first)):
            f.append(first[i])
            f.append(seond[i])
        return f