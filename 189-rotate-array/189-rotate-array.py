class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
        # gind the pivot and reverse both arrays
        