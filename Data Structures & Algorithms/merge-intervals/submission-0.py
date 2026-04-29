class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort the intervals based on the start point
        intervals.sort(key=lambda i:i[0])

        output = [intervals[0]] # start with first intervals
        print("sorted:", intervals)
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            print("lastEnd", lastEnd)
            # overlap detected
            if start <= lastEnd:
                # merge intervals
                print("overlap detected")
                newEnd = max(lastEnd, end)
                output[-1][1] = newEnd
            else:
                output.append([start, end])
        
        return output


        