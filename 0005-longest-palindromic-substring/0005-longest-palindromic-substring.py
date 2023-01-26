class Solution:
    
     def check(self,str1,l,r):
        while l>=0 and r<len(str1) and str1[l]==str1[r]:
            l=l-1
            r+=1
        
        return str1[l+1:r]
    
     def longestPalindrome(self, s: str) -> str:
        res=''
        for i in range(len(s)):
            temp=self.check(s,i,i)
            if len(temp)>len(res):
                res=temp
            temp=self.check(s,i,i+1)
            if len(temp)>len(res):
                res=temp
        return res
    
    