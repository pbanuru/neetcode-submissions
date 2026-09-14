class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(f"{len(word)}.{word}")
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # 4.neet2.co
        # 0123456789
        while i < len(s):
            j = i
            while s[i]!='.':
                i+=1
            wordlen = int(s[j:i])
            word = s[i+1:i+1+wordlen]
            res.append(word)
            i += 1+wordlen
        return res