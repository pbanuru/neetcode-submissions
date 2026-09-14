class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        s = []

        for r,t in enumerate(temperatures):
            while s and t > temperatures[s[-1]]:
                result[s[-1]] = r-s[-1]
                s.pop()
            s.append(r)
        return result
