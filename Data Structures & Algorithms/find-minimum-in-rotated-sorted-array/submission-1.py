class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        high = len(nums) - 1

        # Binary search for the rotation point (the minimum element).
        # lo < high (not <=) so the loop exits with lo == high pointing
        # at the answer, instead of overshooting past it.
        while lo < high:
            mid = (lo + high) // 2

            # If nums[mid] <= nums[high], the right half (mid..high) is
            # sorted, so the minimum is at mid or somewhere to its left.
            # Keep mid in range since it could be the minimum itself.
            if nums[mid] <= nums[high]:
                high = mid
            else:
                # Otherwise the left half is the "big" side of the
                # rotation, so the minimum must be strictly right of mid.
                lo = mid + 1

        return nums[lo]


        