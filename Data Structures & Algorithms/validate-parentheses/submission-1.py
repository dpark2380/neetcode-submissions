class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {'(': ')', '{': '}', '[':']'}

        stack = []

        for c in s:
            # Opening bracket
            if c in mappings:
                stack.append(c)
            else:
                # Closing bracket

                # Popping what should be the corresponding opening bracket.
                if not stack:
                    return False
                cur = stack.pop()
                if mappings[cur] != c:
                    return False
        
        if stack:
            return False
        
        return True