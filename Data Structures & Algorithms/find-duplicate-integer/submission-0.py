class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        repeated = set()
        for n in nums:
            if n in repeated:
                return n
            repeated.add(n)
        return nums[0]