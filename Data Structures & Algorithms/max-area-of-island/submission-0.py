class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        finalCount = 0
        n = len(grid)
        m = len(grid[0])

        directions = [[-1,0] , [1,0] , [0,-1] , [0,1]]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    stack = []
                    stack.append([i,j])
                    count = 0
                    while stack:
                        count += 1
                        r,c = stack.pop()
                        for nr,nc in directions:
                            dr,dc = r + nr , c + nc
                            if 0 <= dr < n and 0 <= dc < m:
                                if grid[dr][dc] == 1:
                                    stack.append([dr,dc])
                                    grid[dr][dc] = 0
                    finalCount = max(finalCount,count)
                    
        return finalCount