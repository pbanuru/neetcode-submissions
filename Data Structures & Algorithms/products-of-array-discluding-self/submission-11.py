class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 8, 24]
        # [48,48,24,6]

        # [6,24,48,48]

        l,r = [],[]
        for v in nums:
            l.append(l[-1]*v if l else v)
        for v in reversed(nums):
            r.append(r[-1]*v if r else v)
        r.reverse()
        print(l)
        print(r)
        res = []
        for i in range(len(nums)):
            left = l[i-1] if i-1>=0 else 1
            right = r[i+1] if i+1<len(nums) else 1
            res.append(left*right)
        return res

                
        