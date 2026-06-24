class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        # s = re.sub(r'[^a-z0-9]', '', s)

        end = len(s) - 1

        for i in range(len(s)):
            if s[i] != s[end]:
                return False
            
            end = end - 1
        
        return True