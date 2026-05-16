class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
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
        even = (len(self.maxHeap) + len(self.minHeap)) % 2 == 0

        if even:
            return (-self.minHeap[0] + self.maxHeap[0]) / 2
        else:
            return -self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else self.maxHeap[0]
        