class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        checked = {}

        for n in nums:
            checked[n] = 1+ checked.get(n, 0)
        arr = []
        for num, count in checked.items():
            arr.append([count, num])
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
    
        return res
        
