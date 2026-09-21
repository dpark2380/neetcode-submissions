class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            else:
                second = stack.pop()
                first = stack.pop()
                if tok == '+':
                    num = first + second
                elif tok == '-':
                    num = first - second
                elif tok == '*':
                    num = first * second
                elif tok == '/':
                    # Just dividing first and second would give an integer result that is rounded towards
                    # negative infinity. Need to convert one number to float. 
                    # Applying int to float result then truncates towards zero.
                    num = int(first / float(second))
                stack.append(num)
        
        return stack.pop()