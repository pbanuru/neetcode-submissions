class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        matches = 0

        for c in s1:
            c1[c]+=1
        
        l = 0
        for r in range(len(s2)):
            c2[s2[r]]+=1
            if c2[s2[r]] == c1.get(s2[r],0):
                matches += 1
    
            while (r-l+1 > len(s1)):
                if c2[s2[l]] == c1.get(s2[l],0):
                    matches -= 1
                c2[s2[l]] -= 1
                l+=1
            
            if matches == len(c1):
                return True
        return False
            