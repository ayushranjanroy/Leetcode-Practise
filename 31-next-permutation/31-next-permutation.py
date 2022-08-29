class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i=j= len(nums)-1
        while(i>0):
            if(nums[i]>nums[i-1]): break
            i -= 1
        i -= 1      # first decreasing number
        
        while(j>i): # find next greater to nums[i]
            if(nums[j]>nums[i]): break
            j -= 1
            
        nums[i],nums[j] = nums[j],nums[i] # swap
        nums[i+1:] = sorted(nums[i+1:])   # sort
        
        