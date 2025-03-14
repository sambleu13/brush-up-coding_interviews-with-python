import heapq

class MiddleElementFinder:
    def __init__(self):
        self.heaps = [], []

    def add_num(self, num: int) -> None:
        # implement this
        large, small = self.heaps
        heapq.heappush(large, -heapq.heappushpop(small, -num))
        if len(small) < len(large):
            heapq.heappush(small, -heapq.heappop(large))


    def middle_element(self) -> int:
        # implement this
        large, small = self.heaps
        if (len(small) % 2 == 0 and len(large) % 2 == 0) or ((len(small) + len(large)) % 2 == 0):
            return -small[0] if -small[0] > large[0] else large[0]
        else:
            return -heapq.heappop(small)

# Let's test the code
estimate_finder = MiddleElementFinder()
estimate_finder.add_num(5)
estimate_finder.add_num(10)
estimate_finder.add_num(3)
estimate_finder.add_num(1)
estimate_finder.add_num(7)
estimate_finder.add_num(2)


print(estimate_finder.middle_element()) # Expected output: 5
