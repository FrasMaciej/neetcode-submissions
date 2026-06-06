class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1
        while l <= r:
            mid_index = (l + r) // 2
            row = mid_index // cols
            col = mid_index % cols
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                r = mid_index - 1
            if matrix[row][col] < target:
                l = mid_index + 1
        return False