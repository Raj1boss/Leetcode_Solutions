class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count=0
        for i in range(left,right+1):
            if words[i][-1] in ['a','i','o','u','e'] and words[i][0] in ['a','i','o','u','e']:
                count+=1
        return count