class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        ops = {"+", "-", "*", "/"}
        for r,c in enumerate(tokens):
            if c not in ops:
                s.append(int(c))
            else:
                b,a = s.pop(), s.pop()
                if c == '+':
                    s.append(a+b)
                elif c=='-':
                    s.append(a-b)
                elif c == '*':
                    s.append(a*b)
                else:
                    s.append(int(a/b))
        return s[0]

                
            