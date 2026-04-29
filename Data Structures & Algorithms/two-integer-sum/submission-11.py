class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        targetMap = {}
        for i, num in enumerate(nums):
            print("i: ", i)
            print("num: ", num)

            diff = target - num
            if diff in targetMap:
                return [targetMap[diff], i]
            else:
                targetMap[num] = i
        return []
        