class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        # area = min(heights[i], heights[j]) * (j - i)

        # initialize output
        maxArea = 0
        # iterate through heights with 2 pointers
        l, r = 0, len(heights)-1

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            maxArea = max(curr_area, maxArea)
            
            # move forward from the smaller bar
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
