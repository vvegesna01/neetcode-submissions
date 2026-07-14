class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # base cases
        # if new interval goes at the start
        if not intervals:
            return [newInterval]

        newStart = newInterval[0]
        newEnd = newInterval[1]
        output = []

        # if newEnd < intervals[0][0]:
        #     output.append(newInterval)
        #     output.append(intervals)
        #     return output

        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            newInterval[0] = newStart
            newInterval[1] = newEnd
            i += 1
        
        output.append(newInterval)
        while i < n:
            output.append(intervals[i])
            i += 1
        
        return output










        