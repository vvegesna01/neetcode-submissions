class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # numbers -> increasing order

        # return [ind1, ind2]; nums[ind1] + nums[ind2] = targer

        stack = dict()
        res = []
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in stack:
                return [stack[diff] + 1, i+1]
            else:
                stack[num] = i
        
        return res
