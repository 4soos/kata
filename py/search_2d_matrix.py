from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n, j = len(matrix), len(matrix[0]), 0

        while m >= 0 and j < n:
            if matrix[m][j] == target: return True
            elif matrix[m][j] > target: m -= 1
            else: j += 1
        return False

