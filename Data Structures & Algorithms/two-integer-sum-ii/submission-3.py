class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # intialise visited dict
        visited = dict() # key: numbers, val: index

        # iterate through numbers
        for i, num in enumerate(numbers):
            diff = target - num
            # check if target-num in visited, return indices in order
            if diff in visited.keys():
                return [visited[diff] + 1, i+1]

            # if diff not in visited, add to visited
            else:                
                visited[num] = i
        
        return None

# time complexity: O(n)
# space complexity: O(n)