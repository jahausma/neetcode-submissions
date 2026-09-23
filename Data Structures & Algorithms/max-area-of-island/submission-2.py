class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        
        def bfs(row,col):

            q = collections.deque()
            visit.add((row,col))
            q.append((row,col))
            area = 1

            while q:
                r,c = q.popleft()
                dirs = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in dirs:
                    r_nbr = dr + r
                    c_nbr = dc + c
                    if ((r_nbr in range(rows)) 
                         and (c_nbr in range(cols))
                         and (r_nbr,c_nbr) not in visit
                         and grid[r_nbr][c_nbr] == 1):
                            area += 1
                            q.append((r_nbr,c_nbr))
                            visit.add((r_nbr,c_nbr))
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] not in visit and grid[r][c] == 1:
                    maxArea = max(maxArea,bfs(r,c)) # use outer loop to track max
            
        return maxArea



            
