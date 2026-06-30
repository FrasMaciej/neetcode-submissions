class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pacific_visited = set()
        atlantic_visited = set()
    
        res = []

        def dfs(r, c, ocean, prev):
            if r == ROWS or c == COLS or r < 0 or c < 0 or prev > heights[r][c] or (r, c) in ocean:
                return
            ocean.add((r,c))
            for move_r, move_c in directions:
                dfs(r + move_r, c + move_c, ocean, heights[r][c])      
    
        # cells across the row 
        for c in range(COLS):
            dfs(0, c, pacific_visited, heights[0][c])
            dfs(ROWS - 1, c, atlantic_visited, heights[ROWS -1][c])   
        # cells across the column
        for r in range(ROWS):
            dfs(r, 0, pacific_visited, heights[r][0])
            dfs(r, COLS - 1, atlantic_visited, heights[r][COLS -1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    res.append([r, c])

        return res

