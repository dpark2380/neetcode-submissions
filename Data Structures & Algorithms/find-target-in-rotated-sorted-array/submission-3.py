class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        # +1 for strict inequality, 
        # no +1 for equal to or inequality

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            
            # In left sorted part
            if nums[lo] <= nums[mid]:
                # 1st case, left sorted part not ended yet, search rest of left sorted part
                # 2nd case, target in right sorted part.
                if target > nums[mid] or target < nums[lo]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                # In right sorted part
                # 1st case, left side of right sorted part not ended, search rest.
                # 2nd case, target in left sorted part.
                if target < nums[mid] or target > nums[hi]:
                    hi = mid - 1
                else:
                    lo = mid + 1

        
        return -1
