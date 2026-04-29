class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        res = []
        for num, cnt in count.items():
            res.append([cnt, num])
        res.sort()

        arr = []
        while len(arr) < k:
            arr.append(res.pop()[1])
        
        return arr