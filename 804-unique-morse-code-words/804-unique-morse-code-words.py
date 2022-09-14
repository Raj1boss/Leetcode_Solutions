class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d=set()
        letter=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        charcter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in range(len(words)):
            s=''
            for j in words[i]:
                if j in charcter:
                    index_val=charcter.index(j)
                    s=s+letter[index_val]

            d.add(s)
        return len(d)
