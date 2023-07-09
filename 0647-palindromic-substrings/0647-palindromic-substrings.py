class Solution:
    def check(self,str1,l,r,p):
        while l>=0 and r<len(str1) and str1[l]==str1[r]:
            p.append(str1[l:r+1])
            l=l-1
            r+=1
            
    def countSubstrings(self, s: str) -> int:
        res=''
        p=[]
        for i in range(len(s)):
            self.check(s,i,i,p)
            self.check(s,i,i+1,p)
        return len(p)
        
        