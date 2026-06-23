class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        self.fresh = 0
        q = deque()

        def process_cell(row, col):
            if row == ROWS or col == COLS or row < 0 or col < 0 or grid[row][col] != 1:
                return
            q.append((row, col))
            grid[row][col] = 2
            self.fresh -= 1

        minutes = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    self.fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        
        while self.fresh > 0 and q:
            for i in range(len(q)):
                row, col = q.popleft()
                process_cell(row + 1, col)
                process_cell(row - 1, col)
                process_cell(row, col + 1)
                process_cell(row, col - 1)
            minutes += 1
                
        return minutes if self.fresh == 0 else -1
                