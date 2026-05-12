class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)

        buckets = [[] for i in range(len(nums) + 1)]
        for n,f in d.items():
            buckets[f].append(n)
        
        res = []
        for bucket in buckets[::-1]:
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    return res
