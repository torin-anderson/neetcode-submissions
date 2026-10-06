#BFS problem, we can keep a counter for islands and when we run into a 1 we search and find everywhere the island spans. We add ontot the island counter and convert all the 1's part of that island to 0 since we have seen it
#Time O(m * n) where m is the width adn n is the height because at worst we ahve to go through the entire grid twice
#Space O(m * n) too because at worst we add every value from the grid to the queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        queue = collections.deque()

        direction = [(-1,0), (1,0), (0,1), (0,-1)]

        height, width = len(grid), len(grid[0])

        for row in range(height):
            for col in range(width):
                if grid[row][col] == "1":
                    num += 1
                    queue.append((row, col))

                    while queue:
                        rVal, cVal = queue.popleft()
                        grid[rVal][cVal] = "0"
                        for dy, dx in direction:
                            if 0 <= rVal + dy < height and 0<= cVal + dx < width and grid[rVal + dy][cVal + dx] == "1":
                                queue.append((rVal + dy, cVal + dx))

        return num
        