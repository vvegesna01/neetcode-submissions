class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # intervals = [[1, 3], [1, 5], [6, 7]]
        # output = [[1, 3], [1, 5]

        intervals.sort(key=lambda pair:pair[0])

        output = [intervals[0]]

        for i in range(1, len(intervals)):
            lastEnd = output[-1][1]
            start = intervals[i][0]
            end = intervals[i][1]

            # overlap detected
            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)
            
            else:
                output.append([start, end])
        
        return output

