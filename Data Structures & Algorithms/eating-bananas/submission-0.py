class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        mid = (low + high) // 2
        cur = 0

        while low < high:
            mid = (low + high) // 2

            for i in range(len(piles)):
                cur += math.ceil(piles[i] / mid)
            
            if cur <= h:
                high = mid
            else:
                low = mid + 1
            
            cur = 0
    
        return low

