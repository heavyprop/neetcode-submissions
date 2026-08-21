class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # a set
        # a dfs or bfs

        searched = set()
        islands = 0
        stack = []
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1" and (x,y) not in searched:
                    
                    stack.append((x, y))
                    islands += 1

                    while stack:
                        (x, y) = stack.pop()
                        searched.add((x, y))

                        if x + 1 < len(grid):
                            if grid[x + 1][y] == "1" and (x + 1,y) not in searched:
                                stack.append((x + 1, y))

                        if x - 1 >= 0:
                            if grid[x - 1][y] == "1" and (x - 1,y) not in searched:
                                stack.append((x - 1, y))

                        if y + 1 < len(grid[0]) and (x,y + 1) not in searched:
                            if grid[x][y + 1] == "1":
                                stack.append((x, y + 1))

                        if y - 1 >= 0:
                            if grid[x][y - 1] == "1" and (x,y - 1) not in searched:
                                stack.append((x, y - 1))
        
        return islands