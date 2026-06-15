class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2 ** 31 - 1
        visted = set()
        q = deque()

        def addTreasure(r, c):
            if (r in range(ROWS) and
                c in range(COLS) and
                grid[r][c] != -1 and
                (r, c) not in visted):
                    q.append((r, c))
                    visted.add((r, c))

        # Adding all treasures points
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0 and (r,c) not in visted:
                    q.append((r,c))
                    visted.add((r,c))

        
        # starting bfs on treasure points alternatively & updating the neighbors      
        dist = 0
        while q:
            # initially q = [1st, 2nd] treasure points
            # then update q's 1st treasure neighbors with 1 and add to q which aren't visited
            # then update q's 2nd treasure neighbors with 1 and add to q which aren't visited
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addTreasure(r + 1, c)
                addTreasure(r - 1, c)
                addTreasure(r, c + 1)
                addTreasure(r, c - 1)
                
            dist += 1

     

            


        
        