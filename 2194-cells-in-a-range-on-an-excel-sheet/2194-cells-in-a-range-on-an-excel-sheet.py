class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        d=[]
        d.append("A")
        for i in range(1,25+1):
            d.append(chr(ord("A")+i))
            
        index_k=d.index(s[0])
        index_L=d.index(s[3])
        m=d[index_k:index_L+1]
        
        out=[]
        for i in range(len(m)):
            k=[]
            for j in range(int(s[1]),int(s[4])+1):
                k.append(f"{m[i]}{j}")
            out.extend(k)
        return out

        