class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return 1       
        left, right = 0, 1
        while right < n:
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left+1] = nums[right]
                left += 1
        return left + 1