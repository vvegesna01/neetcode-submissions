class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # not overlap if
            if start >= prevEnd:
                #update prevEnd if not overlap
                prevEnd = end
            
            # overlap detected
            else:
                # remove one interval
                res += 1

                # remove the one that ends first
                prevEnd = min(end, prevEnd)
        
        return res

