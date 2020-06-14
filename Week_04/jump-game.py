class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        endreachable = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= endreachable:
                endreachable = i
        return endreachable == 0