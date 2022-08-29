class Solution:
    def check(self, nums: List[int]) -> bool:
        sortcheck = sorted(nums)
        for i in range(len(nums)):
            if(nums[i:] + nums[:i]==sortcheck):
                return True
        return False
        