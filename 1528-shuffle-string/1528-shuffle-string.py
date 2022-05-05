class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_s=''
        for i in range(len(s)):
            for j in range(len(indices)):
                if i==indices[j]:
                    new_s=new_s+s[j]
        return new_s