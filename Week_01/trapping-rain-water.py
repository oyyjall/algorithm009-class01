class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        maxArea, maxleft, maxright = 0, 0, 0
        left, right = 0, n-1
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxleft:
                    maxleft = height[left]
                else:
                    maxArea += (maxleft - height[left])
                left += 1
            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    maxArea += (maxright - height[right])
                right -= 1
        return maxArea