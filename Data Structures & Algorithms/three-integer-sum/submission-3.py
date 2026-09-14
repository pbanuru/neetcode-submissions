class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            j,k = i+1, len(nums)-1
            while j < k:
                total = nums[i]+nums[j]+nums[k]
                if total == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif total > 0:
                    k-=1
                elif total < 0:
                    j += 1
        return [[a,b,c] for a,b,c in res]