"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])


        
        start_ptr = 0
        end_ptr = 0

        meetings = 0
        maxMeetings = 0

        while start_ptr < len(intervals):

            # getting min of both times
            if start_times[start_ptr] < end_times[end_ptr]:
                start_ptr += 1
                meetings += 1
            else:
                end_ptr += 1
                meetings -= 1
            
            maxMeetings = max(meetings, maxMeetings)

        
        return maxMeetings


        
