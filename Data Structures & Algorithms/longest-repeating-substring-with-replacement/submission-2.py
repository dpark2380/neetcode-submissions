class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s is None:
            return 0
        
        left = 0
        counts = defaultdict(int)
        maxCount = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            if counts[s[right]] > maxCount:
                maxCount = counts[s[right]]
            
            length = right - left + 1
            if length - maxCount > k:
                counts[s[left]] -= 1
                left += 1
        
        length = right - left + 1
        return length

