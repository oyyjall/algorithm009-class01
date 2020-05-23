class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        hash_map = {}
        for i in range(0, len(nums)):
            temp = target - nums[i]
            if temp not in hash_map:
                hash_map[nums[i]] = i
            else:
                return [hash_map[temp], i]