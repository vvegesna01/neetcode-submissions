class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in hashmap.keys():
                return [hashmap[diff] + 1, i+1]
            else:
                hashmap[n] = i
        
        return []