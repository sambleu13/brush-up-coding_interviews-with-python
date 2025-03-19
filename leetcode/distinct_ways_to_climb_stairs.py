class Solution:
    def climbStairs(self, n: int) -> int:
        # first declare edge cases
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        # create list of n lenght with one values
        ways = [1]*(n)
        # set initial values for recursive sum
        ways[1] = 2
        # cycle from 2 to n to obtain the number of ways
        # that is the sum of n-1 and n-2 ways
        for i in range(2, n):
            ways[i] = ways[i-1] + ways[i-2]
        # return the last position in the list of n length,
        # so the position is n-1, because list starts in zero
        return ways[n-1]
