class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
     rows = len(grid)
     cols = len(grid[0]) 
     visited = set()
     queue = deque()
     directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]
   
     def bfs(r, c):
        queue.append((r,c))
        visited.add((r,c))
        perim = 0 
        while queue:
           r,c = queue.popleft()
           for dr, dc in directions:
            nr,nc = r + dr , c + dc
            if( nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0 ):
             perim += 1
             
            elif (nr, nc) not in visited:
             visited.add((nr, nc))
             queue.append((nr, nc))
        return perim       
         
         
        
     for r in range(rows): 
        for c in range(cols):
            if grid[r][c] == 1:
               return bfs(r, c)
     return 0        

