class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for anagram in strs:
            li = [0]*26
            for v in anagram:
                li[ord(v)-ord('a')]+=1
            groups[tuple(li)].append(anagram)
        
        return list(groups.values())