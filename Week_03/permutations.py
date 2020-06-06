class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.res = []
        self.backtrack(nums, [])
        return self.res

    def backtrack(self, nums, track):
        if len(track) == len(nums):
            self.res.append(track.copy())
            return
        for i in range(0, len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            self.backtrack(nums, track)
            track.pop()