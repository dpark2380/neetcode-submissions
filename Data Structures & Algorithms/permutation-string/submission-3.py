class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        counts = Counter(s1)

        left = 0
        right = len(s1) - 1
        
        curcounts = Counter(s2[left:right+1])

        while right < len(s2):
            if counts == curcounts:
                return True
            
            # If we checked the last possible window 
            # and didn't return true, then return false. 
            if right == len(s2) - 1:
                return False
            
            curcounts[s2[left]] -= 1
            left += 1
            right += 1
            curcounts[s2[right]] += 1
        
        return False




