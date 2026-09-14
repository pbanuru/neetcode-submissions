class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = defaultdict(int)
        c2 = defaultdict(int)

        for c in s1:
            c1[c]+=1
        
        l = 0
        for r in range(len(s2)):
            c2[s2[r]]+=1
            while (r-l+1 > len(s1)):
                c2[s2[l]] -= 1
                if c2[s2[l]] == 0:
                    del c2[s2[l]]
                l+=1
            
            if c1.items() == c2.items():
                return True
        return False
            