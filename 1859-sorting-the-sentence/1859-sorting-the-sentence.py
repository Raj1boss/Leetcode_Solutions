class Solution:
    def sortSentence(self, s: str) -> str:
        new=''
        for i in sorted(s.split(),key=lambda x:x[-1]):
            new=new+i[:-1]+" "
        return new.strip()