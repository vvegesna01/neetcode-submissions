class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):

            # 1: newInterval goes before currIntervals
            if newInterval[1] < intervals[i][0]:
                #insert new interval first
                res.append(newInterval)
                # add the rest of the intervals
                return res + intervals[i:]
            
            # 2: newInterval goes after currIntervals
            # newinterval could still be overlapping with intervals to the right
            elif newInterval[0] > intervals[i][1]:
                # insert currInterval first
                res.append(intervals[i])
            
            # 3: newInterval is overlapping with currInterval
            else:
                # merge newInterval with currInterval
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

                # don't add newInterval yet since it could still be overlapping
        
        res.append(newInterval)
        return res



                

