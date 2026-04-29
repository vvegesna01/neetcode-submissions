class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        stack = []
        for n in nums:
            if n in stack:
                return True
            else:
                stack.append(n)
        
        return False