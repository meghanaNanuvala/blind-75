class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if not self.minHeap or num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap, num)
        
        # uneven size
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, val)
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        
    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        
        return (self.minHeap[0] + self.maxHeap[0]) / 2

        
        