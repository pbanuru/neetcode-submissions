class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)

        product = 1
        for i,v in enumerate(nums):
            output[i] = product
            product = v * product

        product = 1
        for i,v in reversed(list(enumerate(nums))):
            output[i]*=product
            product = v * product
        
        return output