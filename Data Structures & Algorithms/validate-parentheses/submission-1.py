class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(',']':'[','}':'{'}
        # brackets = {'(':')','[':']','{':'}'}
        stack = []
        for e in s:
            if e in brackets.values():
                stack.append(e)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                if temp != brackets[e]:
                    return False
        return len(stack)==0
