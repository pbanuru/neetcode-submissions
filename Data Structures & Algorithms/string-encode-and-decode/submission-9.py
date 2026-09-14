class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')
        return "".join(res)

    # 4#neet4#code
    # 01234456789

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i+=1
                if s[i] == '#':
                    res.append(s[i+1:i+1+num])
                    i+=num+1
        return res
        

                
            

