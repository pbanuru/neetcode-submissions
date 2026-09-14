class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1]*len(nums)
        rightProducts = [1]*len(nums)

        product = 1
        for i,v in enumerate(nums):
            leftProducts[i] = product
            product = v * product
        product = 1
        for i,v in reversed(list(enumerate(nums))):
            rightProducts[i] = product
            product = v * product
        
        output = [1]*len(nums)
        for i in range(len(nums)):
            left = leftProducts[i]
            right = rightProducts[i]
            output[i] = left*right
        return output
            