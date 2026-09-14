class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        group = set()
        for r in range(len(s)):
            while s[r] in group:
                group.remove(s[l])
                l+=1
            group.add(s[r])
            res = max(res, len(group))
        return res