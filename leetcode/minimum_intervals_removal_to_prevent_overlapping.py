# return the mininum number of intervals to make the intervals non-overlapping
# best solution yet:
# - sorting by key = end interval, 
# -simple iterations that compare min_ed with the start to remove less intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        min_ints = 0
        if len(intervals) > 1:
            min_end = float('-inf')
            for start, end in sorted(intervals, key=lambda x: x[1]):
                if start >= min_end:
                    min_end = end
                else:
                    min_ints += 1
                print(start, end, min_end)

        return min_ints
