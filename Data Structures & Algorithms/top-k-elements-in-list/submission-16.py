class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create hashmap for freq
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # build list of [freq, num] pairs from hashmap
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])

        # sort based on freq
        arr.sort()

        # create empty result set
        res = []

        # pop highest freq and append to results
        while len(res) < k:
            res.append(arr.pop()[1]) 

        # return results
        return res