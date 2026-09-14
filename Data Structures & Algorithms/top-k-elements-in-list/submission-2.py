
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = [(-count, c) for c, count in counts.items()]
        heapq.heapify(heap)
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res
