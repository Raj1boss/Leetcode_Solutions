class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        new=[]
        for i in range(len(matrix)):
            for j in matrix[i]:
                new.append(j)
        srt_1=sorted(new)
        
        return srt_1[k-len(new)-1]
        
        
        
        
        
       
        