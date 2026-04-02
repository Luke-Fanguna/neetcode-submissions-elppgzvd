class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * m for _ in range(n)]
        grid[0][0] = 1
        q = deque([(0,1), (1,0)])
        seen = set()
        while q:
            qlen = len(q)
            for _ in range(qlen):
                x, y = q.popleft()
                carry = 0
                if x >= n or y >= m or (x,y) in seen:
                    continue
                seen.add((x,y))
                if x - 1 >= 0:
                    carry += grid[x-1][y]
                if y - 1 >= 0:
                    carry += grid[x][y-1]
                grid[x][y] = carry
                q.append((x + 1, y))
                q.append((x, y + 1))
        
        return grid[-1][-1]