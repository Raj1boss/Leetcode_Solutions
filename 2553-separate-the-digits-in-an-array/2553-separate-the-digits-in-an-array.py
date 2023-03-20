class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr_1=list(map(str,nums))
        new_arr=[int(j) for i in range(len(arr_1)) for j in arr_1[i]]
        return new_arr