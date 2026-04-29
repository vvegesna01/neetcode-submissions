class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        targetMap = {}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in targetMap:
                return [targetMap[diff]+1, i+1]
            targetMap[n] = i
        