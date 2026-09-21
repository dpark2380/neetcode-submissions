class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '/', '*'}
        stack = []

        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            else:
                # Second before first
                second = stack.pop()
                first = stack.pop()
                if tok == '+':
                    num = first + second
                elif tok == '-':
                    num = first - second
                elif tok == '*':
                    num = first * second
                elif tok == '/':
                    num = int(first / float(second))
                stack.append(num)

        return stack.pop()