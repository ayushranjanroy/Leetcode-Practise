class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(" ")
        a.reverse()
        ans = ""
        
        for i in a:
            if i=='': continue
            ans += i+' '
        return ans[:-1]
            
        