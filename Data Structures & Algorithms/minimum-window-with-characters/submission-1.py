class Solution:
    def minWindow(self, s: str, t: str) -> str:
        scount = defaultdict(int)
        tcount = defaultdict(int)

        for c in t:
            tcount[c]+=1

        res = (float('inf'), None)

        matches = 0

        l = 0
        for r in range(len(s)):
            scount[s[r]]+=1
            if scount[s[r]] == tcount.get(s[r], 0):
                matches += 1

            while matches == len(tcount):
                res = min(res, (r-l+1, (l,r)))
                if scount[s[l]] == tcount.get(s[l],0):
                    matches -= 1
                scount[s[l]] -= 1
                l+=1
        
        return s[res[1][0]:res[1][1]+1] if res[1] else ""


            



