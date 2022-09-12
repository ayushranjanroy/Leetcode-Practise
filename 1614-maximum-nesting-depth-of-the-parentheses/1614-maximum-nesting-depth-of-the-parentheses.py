class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = float(-inf)
        c = 0
        for i in s:
            if i=="(": c+=1
            maxi = max(maxi,c)
            if i==")": c-=1
        return maxi