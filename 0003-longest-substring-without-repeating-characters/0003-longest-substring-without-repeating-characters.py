class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<0:
            return 0
        map1={}
        start=0
        max_lenght=0
        for i in range(len(s)):
            if s[i] in map1 and start<=map1[s[i]]:
                start=map1[s[i]]+1
            else:
                max_lenght=max(max_lenght,i-start+1)
            map1[s[i]]=i
        return max_lenght