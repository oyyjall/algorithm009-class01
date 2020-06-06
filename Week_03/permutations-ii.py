class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for p in self.permuteUnique(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + p)
        return res