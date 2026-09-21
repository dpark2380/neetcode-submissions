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

        maxleft = height[left]
        maxright = height[right]

        ans = 0

        while left < right:
            if maxleft < maxright:
                left += 1
                if height[left] < maxleft:
                    ans += maxleft - height[left]
                else:
                    maxleft = height[left]
            else:
                right -= 1
                if height[right] < maxright:
                    ans += maxright - height[right]
                else:
                    maxright = height[right]
        
        return ans

