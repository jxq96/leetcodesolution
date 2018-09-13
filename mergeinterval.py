class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda s: s.start)
        i = 0
        while i + 1 < len(intervals):
            if intervals[i+1].start <= intervals[i].end:
                tmp = Interval(intervals[i].start, max(intervals[i].end,intervals[i+1].end))
                intervals.remove(intervals[i])
                intervals.remove(intervals[i])
                intervals.insert(i, tmp)
            else:
                i += 1
        return intervals