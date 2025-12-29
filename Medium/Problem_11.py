class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_water = 0
        while left < right:
            if height[left] < height[right]:
                max_water = max(max_water,height[left]*(right-left))
                left += 1
            else:
                max_water = max(max_water,height[right]*(right-left))
                right -= 1
        return max_water

        