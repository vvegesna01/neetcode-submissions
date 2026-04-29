class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            
            # if we find a sorted section
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
            
            m = (r + l) // 2
            res = min(res, nums[m])
            # check which portion our pivot is int
            if nums[m] >= nums[l]:
                # search right section
                l = m + 1
            else:
                r = m - 1
        
        return res


 


