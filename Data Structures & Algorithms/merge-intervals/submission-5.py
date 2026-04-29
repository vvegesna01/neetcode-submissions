class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda pair:pair[0])
        merged = [intervals[0]]
        for interval in intervals:
            lastEnd = merged[-1][1]
            # check for overlap
            if interval[0] <= lastEnd:
                merged[-1][1] = max(interval[1], lastEnd)
            
            else:
                merged.append([interval[0], interval[1]])
        
        return merged