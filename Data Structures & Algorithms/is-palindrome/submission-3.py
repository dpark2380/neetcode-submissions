class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = s.lower()
        st = re.sub(r'[^a-zA-Z0-9]', '', low)

        left = 0
        right = len(st) - 1

        while left < right:
            if st[left] != st[right]:
                return False
            left += 1
            right -= 1
        
        return True
