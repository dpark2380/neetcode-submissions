class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            twosum = numbers[left] + numbers[right]
            if twosum > target:
                right -= 1
            elif twosum < target:
                left += 1
            else:
                return [left+1, right+1]

        return [0, 0]