class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max1=-999
        for i in range(len(sentences)):
            count=0
            for j in sentences[i].split():
                count=count+1
            if count>max1:
                max1=count
        return max1
        