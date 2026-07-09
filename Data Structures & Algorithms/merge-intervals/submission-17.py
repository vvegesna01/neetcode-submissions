class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
        if intervals == []:
            return []
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda i:i[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            lastEnd = output[-1][1]

            # overlap detection
            if intervals[i][0] <= lastEnd:
                # merge intervals
                output[-1][0] = min(intervals[i][0], output[-1][0])
                output[-1][1] = max(intervals[i][1], output[-1][1])
            
            else:
                output.append(intervals[i])
        
        return output