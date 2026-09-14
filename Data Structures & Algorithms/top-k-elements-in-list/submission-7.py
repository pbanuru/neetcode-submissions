class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = defaultdict(int)
        for v in nums:
            counts[v]+=1
        
        for num,freq in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif heap[0][0] < freq:
                heapq.heapreplace(heap, (freq,num))

        return [num for _,num in heap]