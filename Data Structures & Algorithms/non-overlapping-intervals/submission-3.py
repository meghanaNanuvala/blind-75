class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x[1])
        prevEnd = intervals[0][1]
        removals = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd: 
                removals += 1
            else:
                prevEnd = intervals[i][1]

        return removals



        
        