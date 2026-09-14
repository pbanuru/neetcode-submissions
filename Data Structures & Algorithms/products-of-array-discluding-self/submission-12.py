class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        l = [1]*N
        r = [1]*N

        # l[i] = product of everything to the left of i
        # l[1] = nums[0]
        # l[2] = nums[0] * nums[1] 
        # l[3] = nums[0] * nums[1] * nums[2]
        
        # l[2] = l[1] * nums[1] 
        # l[3] = l[2] * nums[2]

        # r[i] = product of everything to the right of i
        # [1,2,3,4]
        # r[3] = 1
        # r[2] = nums[3] 
        # r[1] = nums[2] * nums[3] || nums[2] * r[2]
        # r[0] = nums[1] * nums[2] * nums[3] || nums[1] * r[1]
        # r[i] = nums[i+1] * r[i+1]

        for i in range(1,len(nums)):
            l[i] = l[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            r[i] = r[i+1]*nums[i+1]
        return [l[i]*r[i] for i in range(len(nums))]
        
            