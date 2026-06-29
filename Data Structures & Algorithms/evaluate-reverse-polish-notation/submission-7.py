class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operants = ['+','-','*','/']
        for e in tokens:
            if e not in operants:
                stack.append(int(e))
            else:
                b= stack.pop()
                a= stack.pop()
                if e == '+':
                    stack.append(a+b)
                elif e == '-':
                    stack.append(a-b)
                elif e == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack.pop()