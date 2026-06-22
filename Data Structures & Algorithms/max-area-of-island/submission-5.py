class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def get_area(row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            
            area = 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                area += get_area(row + dr, col + dc)
            return area

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, get_area(row, col))
        return max_area