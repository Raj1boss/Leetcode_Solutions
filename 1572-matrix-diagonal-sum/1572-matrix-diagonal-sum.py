class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i=0
        j=0
        l=len(mat)-1
        sum=0
        while i<len(mat):
            if mat[i][j]==mat[i][l] and i==l:
                sum=sum+mat[i][j]
                i=i+1
                j=j+1
                l=l-1
                continue
            
            sum=sum+mat[i][j]+mat[i][l]
            i=i+1
            j=j+1
            l=l-1
        return sum
        
        