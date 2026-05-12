class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for v in nums:
            if v in freq:
                freq[v] += 1
            else:
                freq[v] = 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for v,f in freq.items():
            buckets[f].append(v)
        
        res = []
        for bucket in buckets[::-1]:
            for v in bucket:
                if k != 0:
                    res.append(v)
                    k -= 1
            
        return res