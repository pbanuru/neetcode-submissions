class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for start in num_set:
            if start-1 not in num_set:
                nxt = start+1
                while nxt in num_set:
                    nxt+=1
                longest = max(longest, nxt-start)
        return longest