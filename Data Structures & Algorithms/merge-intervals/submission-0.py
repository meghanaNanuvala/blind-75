class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        res = [intervals[0]]


        for i, interval in enumerate(intervals):
            if res[-1][1] < interval[0]:
                res.append(interval)
            else:
                inv = [min(res[-1][0], interval[0]), max(res[-1][1], interval[1])]
                res[-1] = inv
        
        return res
        