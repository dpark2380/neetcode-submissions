class Solution:
    def trap(self, height: List[int]) -> int:
        # left and right pointers
        # track tallest bar on each side.
        # work inward from side with lower tallest bar. 
        # if shorter than maximum, add difference to total. 
        # Taller, update maximum
        # Go until meet at middle.
        left = 0
        right = len(height) - 1

        ans = 0

        leftmax = height[left]
        rightmax = height[right]

        while left < right:
            if leftmax <= rightmax:
                left += 1
                if height[left] < leftmax:
                    ans += leftmax - height[left]
                else:
                    leftmax = height[left]
            else:
                right -= 1
                if height[right] < rightmax:
                    ans += rightmax - height[right]
                else:
                    rightmax = height[right]
        
        return ans

