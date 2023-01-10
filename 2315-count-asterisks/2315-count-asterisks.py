class Solution:
    def countAsterisks(self, s: str) -> int:
        bars=0
        astr=0
        for i in s:
            if i=="|":
                bars=bars+1
            elif i=="*" and bars%2==0:
                astr+=1
        return astr
        