学习笔记

几种排序的实现：

class Solution:

    def bubble_sort(self, nums):
        if not nums:
            return []
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    def select_sort(self, nums):
        if not nums:
            return []
        for i in range(0, len(nums)):
            minimum = float('inf')
            for j in range(i, len(nums)):
                if nums[j] < minimum:
                    minimum = nums[j]
            nums[i], minimum = minimum, nums[i]
        return nums

    def insert_sort(self, nums):
        if not nums:
            return []
        for i in range(1, len(nums)):
            j = i
            while j > 0:
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    j -= 1
                else:
                    break
        return nums

    def quick_sort(self, nums, first, last):
        if first >= last:
            return
        mid_value = nums[first]
        low, high = first, last
        while low < high:
            while low < high and nums[high] >= mid_value:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] < mid_value:
                low += 1
            nums[high] = nums[low]
        nums[low] = mid_value
        self.quick_sort(nums, first, low - 1)
        self.quick_sort(nums, low + 1, last)
        return nums

    def merge_sort(self, nums, left, right):
        if left >= right:
            return
        mid = (left + right) >> 1
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)
        return nums

    def merge(self, nums, left, mid, right):
        temp = [0 for _ in range(right - left + 1)]
        i, j, k = left, mid + 1, 0
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            temp[k] = nums[i]
            i, k = i+1, k+1
        while j <= right:
            temp[k] = nums[j]
            j, k = j+1, k+1

        for p in range(0, len(temp)):
            nums[left + p] = temp[p]

t = Solution()

nums = [6,2,5,1,4,8,9]

print(t.bubble_sort(nums))

print(t.select_sort(nums))

print(t.insert_sort(nums))

print(t.quick_sort(nums, 0, len(nums)-1))

print(t.merge_sort(nums, 0, len(nums)-1))

