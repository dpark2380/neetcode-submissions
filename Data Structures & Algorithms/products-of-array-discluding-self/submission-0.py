class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        cur = 1
        for i in range(len(nums)):
            ans[i] = cur
            cur *= nums[i]

        cur = 1
        right = len(nums) - 1
        while right >= 0:
            ans[right] *= cur
            cur *= nums[right]
            right -= 1
        
        return ans
