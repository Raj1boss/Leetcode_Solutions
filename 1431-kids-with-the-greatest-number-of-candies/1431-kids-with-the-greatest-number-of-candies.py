class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_arr=[]
        for i in range(len(candies)):
            flag=False
            for j in range(len(candies)):
                if candies[i]+extraCandies>=candies[j]:
                    flag=True
                else:
                    flag=False
                    break
            bool_arr.append(flag)
        return bool_arr