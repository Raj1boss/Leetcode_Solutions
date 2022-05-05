class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        d=[]
        for i in range(len(accounts)):
            sum=0
            for j in accounts[i]:
                sum=sum+j
            d.append(sum)
        return max(d)