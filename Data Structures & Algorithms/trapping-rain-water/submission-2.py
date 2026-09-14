class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxLeft, maxRight = 0,0
        res = 0

        while l<r:
            maxLeft, maxRight = max(maxLeft, height[l]), max(maxRight, height[r])
            shortestWall = min(maxLeft, maxRight)
            if height[l]<height[r]:
                trappable = shortestWall - height[l]
                l+=1
            else:
                trappable = shortestWall - height[r]
                r-=1
            res += trappable
        return res
