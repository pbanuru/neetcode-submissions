class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = -k+1
        d = deque([])
        res = []

        for r in range(len(nums)):
            while d and nums[d[-1]] <= nums[r]:
                d.pop()
            d.append(r)

            if d[0] == l-1:
                d.popleft()
            
            
            if l>=0:
                res.append(nums[d[0]])
            l+=1
        return res