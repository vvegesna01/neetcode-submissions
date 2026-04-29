class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        l = 0
        r = len(heights) - 1
        # area = width * heights
        # area = (r - l + 1) * height[l]

        while l < r:
            curr_area = (r - l) * min(heights[l], heights[r])
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
            maxArea = max(curr_area, maxArea)
        
        return maxArea
