class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ind=0
        if ruleKey=='color':
            ind=1
        elif ruleKey=='name':
            ind=2
        count=0
        for i in range(len(items)):
            if items[i][ind]==ruleValue:
                count=count+1
        return count
                
                
        