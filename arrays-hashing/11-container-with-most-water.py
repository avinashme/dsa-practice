# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        while(left < right):
            local_area = (right - left) *  min(height[left], height[right])
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, local_area)
        return max_area


        
