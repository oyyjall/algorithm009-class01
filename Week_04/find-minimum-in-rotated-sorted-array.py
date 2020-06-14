class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. 双指针
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] > nums[right]:
                left += 1
            else:
                right -= 1
        return nums[left]

        # 2. 二分查找
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = (left + right) >> 1
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return -1