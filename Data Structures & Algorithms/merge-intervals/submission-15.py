class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda pair: pair[0])

        output = [intervals[0]]
        for i in range(len(intervals)):
            lastEnd = output[-1][1]
            
            # overlap detected
            if intervals[i][0] <= lastEnd:
                output[-1][0] = min(output[-1][0], intervals[i][0])
                output[-1][1] = max(output[-1][1], intervals[i][1])
            
            else:
                output.append(intervals[i])
            
        
        return output




