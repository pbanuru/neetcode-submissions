class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        s = []

        for i,h in enumerate(heights):
            while s and heights[s[-1]] > h:
                l = s[-2]+1 if len(s)>1 else 0
                r = i-1
                res = max(res, (r-l+1)*heights[s.pop()])
            s.append(i)
        
        while s:
            l = s[-2]+1 if len(s)>1 else 0
            r = len(heights)-1
            res = max(res, (r-l+1)*heights[s.pop()])

        return res
        
