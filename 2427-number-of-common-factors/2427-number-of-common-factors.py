class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        i=1
        count=0
        while i<=a:
            if a%i==0 and b%i==0:
                count=count+1
            i=i+1
        return count
        