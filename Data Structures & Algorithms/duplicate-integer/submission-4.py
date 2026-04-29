class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = defaultdict()

        for num in nums:
            if num in stack:
                stack[num] += 1
                if stack[num] >= 2:
                    return True
            else:
                stack[num] = 1
        
        return False