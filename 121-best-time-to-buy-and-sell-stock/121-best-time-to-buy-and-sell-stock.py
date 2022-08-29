class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi,mini,= float(-inf),float(inf) # INT_MAX in python: float(inf)
        for price in prices:
            mini = min(mini,price)
            maxi = max(maxi,price-mini)
        return maxi
        