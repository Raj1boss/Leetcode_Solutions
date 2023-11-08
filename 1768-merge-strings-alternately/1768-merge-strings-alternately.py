import itertools
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new=''
        for i,v in itertools.zip_longest(word1,word2,fillvalue=''):
            new=new+"".join(i+v)
        return new
        
        