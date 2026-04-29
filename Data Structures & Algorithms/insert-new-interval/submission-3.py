class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        output = []
        N = len(intervals)
        
        i = 0
        # for all intervals before newInterval
        while i < N and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        while i < N and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        output.append(newInterval)


        # # check for overlap
        # print(i)
        # while i < N and newInterval[0] < intervals[i][1]:
        #     # merge
        #     newInterval[0] = min(intervals[i][0], newInterval[0])
        #     newInterval[1] = max(intervals[i][1], newInterval[1])
        #     i += 1
        
        # output.append(newInterval)

        while i < N:
            output.append(intervals[i])
            i += 1
        
        return output


