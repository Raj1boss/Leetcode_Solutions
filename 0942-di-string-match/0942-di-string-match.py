class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        min1=0
        max1=len(s)
        org=[]
        for i in s:
            if i=="I":
                org.append(min1)
                min1+=1
            else:
                org.append(max1)
                max1-=1
        org.append(min1)
        return org
        