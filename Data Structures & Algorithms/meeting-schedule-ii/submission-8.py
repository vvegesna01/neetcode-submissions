"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start_times = []
        end_times = []
        for i in intervals:
            start_times.append(i.start)
            end_times.append(i.end)
        start_times = sorted(start_times)

        end_times = sorted(end_times)

        max_meetings = 0
        curr_meetings = 0

        start_ptr = 0
        end_ptr = 0

        while start_ptr < len(intervals):

            if start_times[start_ptr] < end_times[end_ptr]:
                curr_meetings += 1
                start_ptr += 1
            else:
                end_ptr += 1
                curr_meetings -= 1
            
            max_meetings = max(max_meetings, curr_meetings)
        
        return max_meetings
