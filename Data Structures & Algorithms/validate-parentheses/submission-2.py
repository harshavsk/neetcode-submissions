class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(','}':'{',']':'['}
        stack = []
        for chare in s:
            if chare in brackets.values():
                stack.append(chare)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                if temp != brackets[chare]:
                    return False
        return len(stack)==0
