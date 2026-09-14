class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        minv, maxv = min(s), max(s)
        res = 1
        l,r = minv, minv
        while r<=maxv:
            if r in s:
                res = max(res, r-l+1)
                r+=1
            else:
                r+=1
                l=r
                
        return res
            

