class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxDistance, step, end = 0, 0, 0
        for i in range(0, len(nums)-1):
            maxDistance = max(maxDistance, nums[i] + i)
            if i == end:
                end = maxDistance
                step += 1
        return step