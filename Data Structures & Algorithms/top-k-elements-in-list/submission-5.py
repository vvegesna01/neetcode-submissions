class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        print("count: ", count)
        print("count.items(): ", count.items())

        arr = []
        for num, c in count.items():
            arr.append([c, num])
        arr.sort()

        print("arr: ", arr)
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res

