class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nex=1
        cur=0
        ans = [0]*len(nums)
        for i in nums:
            if "-" in str(i):
                ans[nex] = i
                nex += 2
            else:
                ans[cur] = i
                cur += 2
        return ans