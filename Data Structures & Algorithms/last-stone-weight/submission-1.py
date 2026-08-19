import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        minHeap = []

        # this will give the largest ones
        for item in stones:
            heapq.heappush(minHeap, -item)
    
        while len(minHeap) > 1:
            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)

            # since negative then the comparison is backwards
            # normally be y - x
            if y != x:
                heapq.heappush(minHeap, x - y)
            
        return -minHeap[0] if minHeap else 0



