class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in words:
            g=set(i)
            flag = False
            for j in g:
                if j not in allowed:
                    flag = True
                    break
            if not flag:
                count += 1
        return count
                
                
            
            
            
        
        
        
        