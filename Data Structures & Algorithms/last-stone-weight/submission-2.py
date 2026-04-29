class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-s for s in stones]

        heapq.heapify(neg_stones)
        print(neg_stones)
        while len(neg_stones) > 1:
            s1 = heapq.heappop(neg_stones)
            s2 = heapq.heappop(neg_stones)

            if s2 > s1:
                heapq.heappush(neg_stones, s1 - s2)

        # neg_stones.append(0)
        return abs(neg_stones[0]) if neg_stones else 0

