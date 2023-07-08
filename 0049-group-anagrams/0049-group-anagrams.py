class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in range(len(strs)):
            w="".join(sorted(strs[i]))
            if w in dic:
                dic[w].append(strs[i])
            else:
                dic[w]=[strs[i]]
        d=[]
        for i in dic:
            d.append(dic[i])
        return d
        
        
        