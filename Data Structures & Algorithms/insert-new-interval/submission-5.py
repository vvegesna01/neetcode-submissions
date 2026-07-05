class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        newEnd = newInterval[1]
        newStart = newInterval[0]
        output = []

        # iterate through all intervals (already sorted)
        for i in range(len(intervals)):
            
            # if newInterval is before currInterval 
            if newEnd < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]
            
            elif newStart > intervals[i][1]:
                output.append(intervals[i])
            
            # overlapping
            else:
                # update newInterval by merging
                mergedStart = min(newInterval[0], intervals[i][0])
                mergedEnd = max(newInterval[1], intervals[i][1])
                newInterval = [mergedStart, mergedEnd]

        output.append(newInterval)
        return output     



