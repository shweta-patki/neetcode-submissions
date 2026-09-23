"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        l = sorted(intervals, key=lambda x:x.start)
        for inter in range(len(l)-1):
            if l[inter].end>l[inter+1].start:
                return False
        return True 