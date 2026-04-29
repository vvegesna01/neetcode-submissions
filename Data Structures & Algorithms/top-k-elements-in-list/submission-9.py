class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        print(count)
        
        res = []
        numsSet = set(nums)
        for n in numsSet:
            res.append([n, count[n]])
        

        print(res)
        res.sort(key=lambda pair: pair[1])
        print("sorted res", res)

        output = []

        for i in range(k):
            output.append(res.pop()[0])
        # while len(output) < k:
        #     print("-len(output)")
        #     print(res[-len(output)][0])
        #     output.append(res[-len(output)][0])

        return output



