class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curlen = 0
        ans = 0
        
        elements = set(nums)
        candidates = []

        for num in nums:
            if num - 1 not in elements:
                candidates.append(num)
        
        for num in candidates:
            while num in elements:
                curlen += 1
                num += 1
            
            ans = max(ans, curlen)

            curlen = 0
        
        return ans

        