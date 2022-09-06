class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, g = [], 0
        for ch in s:
            if ch==')': g-=1 # stop if 0
            if g>0: ans.append(ch)
            if ch=="(": g+=1 # allow appending
        return ''.join(ans)        
        