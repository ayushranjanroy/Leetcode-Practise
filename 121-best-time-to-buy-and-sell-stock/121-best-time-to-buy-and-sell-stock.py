class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi,mini,= 0,float(inf) # INT_MAX in python: float(inf)
                                # and INT_MIN: float(-inf)
        for i in prices:
            mini = min(mini,i)
            profit = i-mini
            maxi = max(maxi,profit)
        return maxi
        