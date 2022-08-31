class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i,n in enumerate(nums):
            if n in mp:
                return[mp[n],i]
            mp[target - n] = i
            
            
        