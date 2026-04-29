class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        print(count)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        print("arr:", arr)

        output = []
        while len(output) < k:
            output.append(arr.pop()[1])

        return output
