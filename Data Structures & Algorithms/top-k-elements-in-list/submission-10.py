import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        print(counter)
        heap = []

        # key: the number, val: the frequency
        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        print("heap:", heap)
        output = []
        for h in heap:
            print(h)
            output.append(h[1])
        
        return output

        