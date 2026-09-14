class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for l in s:
            if l-1 not in s:
                # seq start
                r = l
                while r in s:
                    res = max(res, r-l+1)
                    r+=1
        return res