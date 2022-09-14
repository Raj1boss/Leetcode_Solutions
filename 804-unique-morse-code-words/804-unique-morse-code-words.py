class Solution:

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        character=[]
        for i in range(26):
            chrd=chr(ord('a')+i)
            character.append(chrd)
            
        letters=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            
            
        d=set()
        for i in range(len(words)):
            s=''
            for j in words[i]:
                if j in character:
                    index_v=character.index(j)
                    s=s+letters[index_v]
            d.add(s)
        
        return len(d)
            
            
                    
            
        