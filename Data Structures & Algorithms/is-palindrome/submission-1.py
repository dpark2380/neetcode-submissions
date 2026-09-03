class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', lower)
        start = 0
        end = len(cleaned) - 1
        while start < end:
            if cleaned[start] != cleaned[end]:
                return False
            start += 1
            end -= 1

        return True

