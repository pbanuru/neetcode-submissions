class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0]*len(height)
        mL = 0
        maxR = [0]*len(height)
        mR = 0

        for i, h in enumerate(height):
            mL = max(mL, h)
            maxL[i]=mL
        
        for i, h in reversed(list(enumerate(height))):
            mR = max(mR, h)
            maxR[i]=mR
        
        res = 0
        for i in range(len(height)):
            res += min(maxL[i], maxR[i])-height[i]
        return res

        