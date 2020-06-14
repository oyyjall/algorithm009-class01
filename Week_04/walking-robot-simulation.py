class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        if not commands:
            return 0
        obstacles = set(map(tuple, obstacles))
        dx, dy, x, y = 0, 1, 0, 0
        maxDistance = 0
        for command in commands:
            if command == -1:
                dx, dy = dy, -dx
            elif command == -2:
                dx, dy = -dy, dx
            else:
                for step in range(command):
                    if (x + dx, y + dy) not in obstacles:
                        x, y = x+dx, y+dy
                        maxDistance = max(maxDistance, x * x + y * y)
                    else:
                        break
        return maxDistance