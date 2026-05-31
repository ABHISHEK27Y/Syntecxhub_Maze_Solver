import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        return self.f < other.f

def astar(maze, start, end):
    """
    Returns a list of tuples as a path from the given start to the given end in the given maze
    maze: 2D list where 0 is walkable and 1 is wall
    start: tuple (row, col)
    end: tuple (row, col)
    """
    start_node = Node(start)
    end_node = Node(end)
    
    open_list = []
    closed_list = set()
    
    heapq.heappush(open_list, (start_node.f, id(start_node), start_node))
    
    # define movements (up, down, left, right)
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    rows = len(maze)
    cols = len(maze[0])
    
    open_dict = {start: start_node} # position -> node
    
    while open_list:
        current_node = heapq.heappop(open_list)[2]
        if current_node.position in open_dict:
            del open_dict[current_node.position]
            
        closed_list.add(current_node.position)
        
        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path
        
        # Generate children
        for move in movements:
            node_position = (current_node.position[0] + move[0], current_node.position[1] + move[1])
            
            # Make sure within range
            if node_position[0] < 0 or node_position[0] >= rows or node_position[1] < 0 or node_position[1] >= cols:
                continue
                
            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue
                
            # If in closed list, skip
            if node_position in closed_list:
                continue
                
            # Create new node
            new_node = Node(node_position, current_node)
            
            # Calculate f, g, and h
            new_node.g = current_node.g + 1
            # Manhattan distance
            new_node.h = abs(new_node.position[0] - end_node.position[0]) + abs(new_node.position[1] - end_node.position[1])
            new_node.f = new_node.g + new_node.h
            
            # If node in open list and new node has worse g, skip
            if node_position in open_dict and open_dict[node_position].g <= new_node.g:
                continue
                
            # Add to open list
            open_dict[node_position] = new_node
            heapq.heappush(open_list, (new_node.f, id(new_node), new_node))
            
    return None # Path not found

def print_maze(maze, path=None, start=None, end=None):
    rows = len(maze)
    cols = len(maze[0])
    
    maze_viz = [[" " for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                maze_viz[r][c] = "#"
            else:
                maze_viz[r][c] = "."
                
    if path:
        for r, c in path:
            if maze_viz[r][c] != "#":
                maze_viz[r][c] = "*"
            
    if start:
        maze_viz[start[0]][start[1]] = "S"
    if end:
        maze_viz[end[0]][end[1]] = "E"
        
    for row in maze_viz:
        print("".join(row))
        

if __name__ == '__main__':
    # 0 = empty space, 1 = obstacle
    maze = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    end = (7, 6)

    print("Initial Maze:")
    print_maze(maze, start=start, end=end)
    
    path = astar(maze, start, end)
    
    if path:
        print("\nPath found!")
        print_maze(maze, path, start, end)
        print("Steps:", len(path) - 1)
        print("Path coordinates:", path)
    else:
        print("\nNo path found!")
        
    print("\n--- Testing Unreachable Maze ---")
    maze_unreachable = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    path = astar(maze_unreachable, (0, 0), (2, 2))
    if path:
        print("Path found (unexpected)")
    else:
        print("No path found, as expected.")
