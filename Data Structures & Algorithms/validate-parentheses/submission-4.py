class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(',']':'[','}':'{'}
        stack = []
        for r,c in enumerate(s):
            if c in pairs.values():
                stack.append(c)
            elif stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                return False
        return len(stack)==0