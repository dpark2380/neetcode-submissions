class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix) * len(matrix[0])

        low = 0
        high = length - 1

        while low <= high:
            mid = (low + high) // 2

            midr = mid // len(matrix[0])
            midc = mid % len(matrix[0])

            val = matrix[midr][midc]

            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1

        return False