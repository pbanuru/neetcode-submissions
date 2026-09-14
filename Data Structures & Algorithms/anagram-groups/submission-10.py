class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            sd = defaultdict(int)
            for c in s:
                sd[c]+=1
            counts_per_letter = []
            for c in "abcdefghijklmnopqrstuvwxyz":
                counts_per_letter.append(sd.get(c,0))
            d[tuple(counts_per_letter)].append(s)
        return list(d.values())
