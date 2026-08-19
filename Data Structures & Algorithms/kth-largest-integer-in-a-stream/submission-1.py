import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        
        for item in nums:
            heapq.heappush(self.minHeap, item)
        
        size = len(self.minHeap)
        size -= self.k

        for i in range(size):
            if self.minHeap:
                heapq.heappop(self.minHeap)

            




    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        
        size = len(self.minHeap)
        size -= self.k

        for i in range(size):
            if self.minHeap:
                heapq.heappop(self.minHeap)
            
        smallest = self.minHeap[0]

        return smallest
        


