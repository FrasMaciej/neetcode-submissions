class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque() # (row, col)
        visited = set() # (row, col)

        def add_to_queue(row, col):
            if row == ROWS or col == COLS or row < 0 or col < 0 or (row, col) in visited or grid[row][col] == -1:
                return
            q.append((row, col))
            visited.add((row, col))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                add_to_queue(r + 1, c)
                add_to_queue(r - 1, c)
                add_to_queue(r, c + 1)
                add_to_queue(r, c - 1)
                grid[r][c] = dist

            dist += 1


        