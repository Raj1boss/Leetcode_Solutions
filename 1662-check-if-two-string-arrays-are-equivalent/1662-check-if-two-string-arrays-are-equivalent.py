class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        new1=''
        new2=''
        for i in range(len(word1)):
            new1=new1+word1[i]
        for j in range(len(word2)):
            new2=new2+word2[j]
        
        if new1==new2:
            return True
        else:
            return False
        