class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        self.cur_island = 0

        def traverse_island(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return

            self.cur_island += 1
            grid[row][col] = 0

            for dir_r, dir_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                traverse_island(row + dir_r, col + dir_c)

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 1:
                    self.cur_island = 0
                    traverse_island(row, col)
                    max_island = max(max_island, self.cur_island)

        return max_island