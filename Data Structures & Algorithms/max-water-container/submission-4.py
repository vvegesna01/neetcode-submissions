class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # area = width * height
        # area = (r - l + 1) * (min(heights[l], heights[r]))

        l = 0
        r = len(heights) - 1
        maxArea = 0

        while l <= r:
            print("area being calculated for:", heights[l], heights[r])
            print("width is:", (r - l))
            area = (r - l) * min(heights[l], heights[r])
            maxArea = max(area, maxArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea