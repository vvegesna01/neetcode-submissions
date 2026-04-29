class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        # get frequencies for the given array
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        # convert dict to an array so that in can be sorted
        for num, c in count.items():
            arr.append([c, num])
        # sort array
        arr.sort()
        
        res = []
        # add top k elements from the array into res output
        while len(res) < k:
            # only append the num val which is arr.pop()[1]
            res.append(arr.pop()[1])
        return res
