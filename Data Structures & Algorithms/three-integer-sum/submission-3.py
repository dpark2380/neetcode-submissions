class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                twosum = nums[left] + nums[right]
                if twosum > target:
                    right -= 1
                elif twosum < target:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]
                    ])
                    # We need to move off the current indices anyway so move left and right unconditionally.
                    left += 1
                    right -= 1

                    # If there are duplicates we continue moving the pointer (duplicates are next to each other due to the sorted nature of the arrays)
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1


        return ans

