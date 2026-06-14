class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        curSum = 0
        maxArea = float("-inf")
        visted = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0),(1, 0), (0, -1), (0, 1)]

        def bfs(r, c):
            curSum = 1
            queue = collections.deque()
            visted.add((r,c))
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and 
                    c in range(COLS) and
                    grid[r][c]==1 and
                    (r,c) not in visted):
                        queue.append((r,c))
                        visted.add((r,c))
                        curSum += 1

            return curSum


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1 and (r,c) not in visted:
                    # recursively run bfs on land
                    curSum = bfs(r, c)
                    print("true", (r,c), curSum)
                    maxArea = max(maxArea, curSum)

        return max(maxArea, curSum)

        


                


                



        

        