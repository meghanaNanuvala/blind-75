class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        minutes, fresh = 0, 0
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
                    
            
    
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while q and fresh > 0:

            # This loop is to run bfs on multiple rotten oranges simultaneously to add adjacent fresh oranges as rotten
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1):
                            grid[r][c] = 2
                            q.append((r,c))
                            fresh -= 1

            minutes += 1

        return minutes if fresh == 0 else -1


         # if (r < 0 or r == ROWS or
                    # c < 0 or c == COLS or
                    # grid[r][c] != 1):
                    #     continue
                    # grid[r][c] = 2
                    # q.append((r,c))
                    # fresh -= 1
                    # print(r,c, fresh)
                    


        