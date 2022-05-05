class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        d=first
        new=[]
        new.append(first)
        for i in range(len(encoded)):
            new.append(encoded[i]^d)
            d=encoded[i]^d
        return new