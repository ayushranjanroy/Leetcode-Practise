class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
        # find the pivot and reverse both arrays
        