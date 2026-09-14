class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        p = 0
        while p<len(s):
            num = 0
            while p<len(s) and s[p].isdigit():
                num = num*10 + int(s[p])
                p+=1
            p+=1
            res.append(s[p:p+num])
            p+=num
        return res