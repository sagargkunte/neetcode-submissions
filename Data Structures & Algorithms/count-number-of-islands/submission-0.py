class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        finalCount = 0
        n = len(grid)
        m = len(grid[0])

        directions = [[-1,0] , [1,0] , [0,-1] , [0,1]]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    finalCount += 1
                    grid[i][j] = "0"
                    stack = []
                    stack.append([i,j])
                    while stack:
                        r,c = stack.pop()
                        for nr,nc in directions:
                            dr,dc = r + nr , c + nc
                            if 0 <= dr < n and 0 <= dc < m:
                                if grid[dr][dc] == "1":

                                    stack.append([dr,dc])
                                    grid[dr][dc] = "0"

        return finalCount

