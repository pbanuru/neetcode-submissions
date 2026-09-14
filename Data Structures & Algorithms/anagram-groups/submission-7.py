class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for st in strs:
            counts = [0]*26
            for c in st:
                counts[ord(c)-ord('a')]+=1
            groups[tuple(counts)].append(st)
        return list(groups.values())
