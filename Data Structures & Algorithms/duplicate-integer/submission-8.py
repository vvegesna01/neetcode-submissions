class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        checked = []
        for n in nums:
            if n in checked:
                return True
            else:
                checked.append(n)
        
        return False