class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        contains = []
        for n in nums:
            if n in contains:
                return True
            else:
                contains.append(n)
        
        return False