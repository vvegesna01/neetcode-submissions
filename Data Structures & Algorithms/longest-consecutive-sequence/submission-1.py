class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0 # to store maximum streak length
        store = set(nums) # input list to set for O(1) lookups
        
        for num in nums:
            # for each num, start a new streak count at 0
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res