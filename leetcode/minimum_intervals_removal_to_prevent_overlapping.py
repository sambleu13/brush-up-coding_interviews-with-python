# return the mininum number of intervals to make the intervals non-overlapping
# solution using dictionary and set, improved sorting by key = end interval
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        min_ints = 0
        unique_ints = set()
        ints = {}
        if len(intervals) > 1:
            unique_ints = {tuple(i) for i in intervals}
            sort_ints = sorted(map(list,unique_ints), key=lambda x: x[1])
            min_ints = len(intervals) - len(unique_ints)
            max_end = sort_ints[0][0]
            print(sort_ints, max_end)
            for interval in sort_ints:
                if interval[0] not in ints.keys():
                    if ints is None:
                        ints[interval[0]] = interval[1]
                        max_end = interval[1]
                    else:
                        if interval[0] < max_end:
                            min_ints += 1
                        else: 
                            ints[interval[0]] = interval[1]
                            max_end = interval[1]
                else:
                    if interval[1] != ints[interval[0]]:
                        min_ints += 1
                        if interval[1] < ints[interval[0]]:
                            ints[interval[0]] = interval[1]
                            max_end = interval[1]
                print(interval[0], max_end)

        return min_ints
