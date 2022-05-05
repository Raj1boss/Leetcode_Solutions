class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        value=[]
        for i in range(2):
            value.extend(nums)
        return value
        