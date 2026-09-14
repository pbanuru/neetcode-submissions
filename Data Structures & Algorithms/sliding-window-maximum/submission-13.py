from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        d = deque([])
        l = -k+1

        for r in range(len(nums)):
            while d and nums[d[-1]] <= nums[r]:
                d.pop()

            if d and d[0] == l-1:
                d.popleft()
            d.append(r)
            
            if l >= 0:
                res.append(nums[d[0]])
            
            l+=1
        return res
        


