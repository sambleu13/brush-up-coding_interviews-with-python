# return the mininum number of intervals to make the intervals non-overlapping
# solution using dictionary and set, improved sorting by key = end interval, 
# simplified iterations to just compare the min_ed with the start to remove
# less intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        min_ints = 0
        unique_ints = set()
        ints = {}
        if len(intervals) > 1:
            unique_ints = {tuple(i) for i in intervals}
            sort_ints = sorted(map(list,unique_ints), key=lambda x: x[1])
            min_ints = len(intervals) - len(unique_ints)
            min_end = sort_ints[0][0]
            print(sort_ints, min_end)
            for start, end in sort_ints:
                if start >= min_end:
                    min_end = end
                else:
                    min_ints += 1
                print(start, end, min_end)

        return min_ints
