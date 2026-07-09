class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
        # area = (distance between bars) * height of min bar
        # area = (r - l) * min(heights[l], heights[r])
        maxArea = 0
        l = 0
        r = len(heights)-1

        while l < r:
            currArea = (r - l) * min(heights[l], heights[r])
            # replace maxArea if greater max found
            maxArea = max(maxArea, currArea)

            # find next tallest bar
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxArea