class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        for n in nums:
            if n == target:
                return i
            i += 1
        return -1
        