class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        print(count)
        arr = []
        for num, c in count.items():
            arr.append([c, num])
        arr.sort()
        
        print(arr)
        res = list()

        while len(res) < k:
            res.append(arr.pop()[1])



        return res
