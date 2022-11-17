class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len=0
        count=0
        for i in rectangles:
            small_len=min(i)
            if small_len>max_len:
                max_len=small_len
            
        for i in rectangles:
            small=min(i)
            if max_len==small:
                count+=1
        return count
        