class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        new_sentence = ""
        for i in range(k):
            new_sentence += words[i]+' '
        return new_sentence.strip()
            
                       
            
        