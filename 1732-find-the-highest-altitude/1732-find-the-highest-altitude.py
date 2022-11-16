class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high=0
        sum1=0
        new=[0]*len(gain)
        for i in range(len(gain)):
            sum1=sum1+gain[i]
            new[i]=sum1
        
        for i in new:
            if i>high:
                high=i
        return high
            
        