class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)
    def addNum(self, num: int) -> None:
        if self.maxHeap and num > self.maxHeap[0]:
            heapq.heappush(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap, -num)
        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap): return self.maxHeap[0]
        elif len(self.maxHeap) < len(self.minHeap): return -self.minHeap[0]
        else: return (-self.minHeap[0] + self.maxHeap[0]) / 2 
        