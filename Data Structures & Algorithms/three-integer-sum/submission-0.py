class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        nums.sort()

        n = len(nums)
        res = []

        # first digit
        for i in range(n):
            # if curr num is greater than 0 then should break out of the loop
            if nums[i] > 0:
                break
            # we don't want the same number
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            
            lo, hi = i + 1, n - 1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo+1, hi-1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                
                elif summ < 0:
                    lo += 1
                elif summ > 0:
                    hi -= 1
        
        return res


