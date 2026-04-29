class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # intervals = [[1, 2], [2, 3], [4, 6]]
        # output = [[1, 3], [4, 6]]
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # merge
                output[-1][1] = max(end, lastEnd)
            else:
                output.append([start, end])
        
        return output
