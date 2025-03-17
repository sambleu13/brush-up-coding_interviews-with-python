# return the mininum number of intervals to make the intervals non-overlapping
# solution using dictionary and set
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        min_ints = 0
        unique_ints = set()
        ints = {}
        if len(intervals) > 1:
            unique_ints = {tuple(i) for i in intervals}
            sort_ints = sorted(map(list,unique_ints))
            min_ints = len(intervals) - len(unique_ints)
            for interval in sort_ints:
                if interval[0] not in ints.keys():
                    ints[interval[0]] = interval[0]+1
                else:
                    if interval[1] != ints[interval[0]]:
                        min_ints += 1

        return min_ints
