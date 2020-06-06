class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        major, count = 0, 0
        for num in nums:
            if count == 0:
                major = num
            if num == major:
                count += 1
            else:
                count -= 1
        return major