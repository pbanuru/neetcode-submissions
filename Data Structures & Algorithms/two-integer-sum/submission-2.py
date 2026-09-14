class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target = 7
        # array [3,4,5,6]
        #        0 1 2 3
        # d[3] = 0
        # 
        d = dict()
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]], i]
            d[nums[i]] = i
        return []