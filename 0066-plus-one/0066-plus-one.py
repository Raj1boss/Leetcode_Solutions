class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        d=[]
        for i in digits:
            s=s+str(i)

        for i in str(int(s)+1):
            d.append(int(i))
        return d
            
        
        
        