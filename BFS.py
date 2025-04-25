from collections import deque

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y 
        self.parent = parent

def bfs(grid, start, goal):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([Node(start[0], start[1])])

    visited = set()
    visited.add((start[0], start[1]))
    
    while queue:
        current = queue.popleft()
        
        if (current.x, current.y) == goal:
            return current
        
        for direction in directions:
            new_x, new_y = current.x + direction[0], current.y + direction[1]
            
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append(Node(new_x, new_y, current))
    
    return None

def print_path(node):
    if node is None:
        return
    print_path(node.parent)
    print(f"({node.x}, {node.y})", end=" -> ")

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (4, 4)
    
    destination_node = bfs(grid, start, goal)
    
    if destination_node is None:
        print("No path found!")
    else:
        print("Shortest path found:")
        print_path(destination_node)
