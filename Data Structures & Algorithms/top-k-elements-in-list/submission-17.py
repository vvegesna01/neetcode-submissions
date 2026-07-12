class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        print(count)

        freq_map = []
        for n, cnt in count.items():
            freq_map.append([cnt, n])
        
        print(freq_map)
        freq_map.sort()
        
        output = []
        while len(output) < k:
            output.append(freq_map.pop()[1])
        

        return output
            