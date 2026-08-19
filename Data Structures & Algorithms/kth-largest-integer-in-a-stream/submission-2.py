import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []

        # add the initial numbers to the min heap
        for num in nums:
            heapq.heappush(self.minHeap, num)

            # if the size becomes greater than the k, then pop the smallest one
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # add a number for the add 
        heapq.heappush(self.minHeap, val)

        # if size is greater than k then pop the smallest one
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]