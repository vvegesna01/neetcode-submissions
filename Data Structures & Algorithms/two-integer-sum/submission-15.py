class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # given nums
        # given target

        checkedStack = dict()
        for i, n in enumerate(nums):
            diff = target - n
            # we have found a pair
            if diff in checkedStack:
                return list((checkedStack[diff], i))
            
            else:
                checkedStack[n] = i
        
        return [0, 0]
