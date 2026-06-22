class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        groups = 0

        def traverse_island(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            traverse_island(row - 1, col)
            traverse_island(row, col + 1)
            traverse_island(row + 1, col)
            traverse_island(row, col - 1)

        for row in range (0, len(grid)):
            for col in range (0, len(grid[0])):
                if grid[row][col] == "1":
                    groups += 1
                    traverse_island(row, col)

        return groups