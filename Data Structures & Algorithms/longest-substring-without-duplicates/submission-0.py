class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curset = set()
        ans = 0

        left = 0
        
        for right in range(len(s)):
            while s[right] in curset:
                curset.remove(s[left])
                left += 1
            
            curset.add(s[right])
            ans = max(ans, len(curset))
        
        return ans
