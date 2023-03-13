# Imports required for the program
import time
from collections import deque


def maze_find_states(maze):
    """
    Finds the start and goal state, on the maze upper and lower wall

    Args
        maze: The 2D array of the maze
    
    Returns
        start: The coordinates the search is starting from
        goal: The coordinates of the goal state
    """
    maze_ceiling_wall = maze[0]
    maze_floor_wall = maze [-1]

    return (0, maze_ceiling_wall.index(1)), (len(maze) - 1, maze_floor_wall.index(1))


def maze_to_array(filename):
    """
    Reads the maze from within a file and returns the maze as a 2D array the
    program can interpret

    Args:
        filename: takes in the filename formatted the same as the text file
    
    Returns:
        convert_to_binary(contents): Returns the maze from the file read as a 
        2d array and the # replaced with a 0 and the - replaced with a 1
    """
    # Open the file and strip any unnecessary characters
    with open(filename, "r") as file:
        contents = file.read().splitlines()
        contents = [list(row.replace(" ", "")) for row in contents if row.strip()]
   
    def convert_to_binary(arr):
        """
        Converts the maze into a the correct format for the program
        """
        converted = []
        for row in arr:
            converted_row = []
            for element in row:
                if element == "#":
                    converted_row.append(0)
                else:
                    converted_row.append(1)
            converted.append(converted_row)
        return converted

    return convert_to_binary(contents)


def breadth_first_searchOriginal(maze, start, end):
    """
    Performs the breadth first search on the maze specified

    Args:
        maze: The maze read from the file and converted to the binary format
        start: The starting coordinates of the ceiling starting node
        end: The end coordinates on the floor of the maze

    Returns:
        shortest_path: An array of the coordinates as a set for the shortest 
                       path found by the algorithm
        num_nodes_explored: The number of nodes the algorithm had to explore 
                            before finding the end node
    
    """
    ROW, COL = len(maze), len(maze[0])

    def is_valid(row, col):
        return 0 <= row < ROW and 0 <= col < COL and maze[row][col] == 1

    def BFS(row, col):
        q = deque([(row, col, 0, [(row, col)])])
        visited = [[False for _ in range(COL)] for _ in range(ROW)]
        visited[row][col] = True
        nodes_explored = 0
        path = []

        while q:
            curr_row, curr_col, dist, curr_path = q.popleft()
            nodes_explored += 1

            if (curr_row, curr_col) == (end[0], end[1]):
                path = curr_path
                break

            if is_valid(curr_row + 1, curr_col) and not visited[curr_row + 1][curr_col]:
                q.append((curr_row + 1, curr_col, dist + 1, curr_path + [(curr_row + 1, curr_col)]))
                visited[curr_row + 1][curr_col] = True
            if is_valid(curr_row - 1, curr_col) and not visited[curr_row - 1][curr_col]:
                q.append((curr_row - 1, curr_col, dist + 1, curr_path + [(curr_row - 1, curr_col)]))
                visited[curr_row - 1][curr_col] = True
            if is_valid(curr_row, curr_col + 1) and not visited[curr_row][curr_col + 1]:
                q.append((curr_row, curr_col + 1, dist + 1, curr_path + [(curr_row, curr_col + 1)]))
                visited[curr_row][curr_col + 1] = True
            if is_valid(curr_row, curr_col - 1) and not visited[curr_row][curr_col - 1]:
                q.append((curr_row, curr_col - 1, dist + 1, curr_path + [(curr_row, curr_col - 1)]))
                visited[curr_row][curr_col - 1] = True

        return path, nodes_explored

    shortest_path, num_nodes_explored = BFS(start[0], start[1])
    return shortest_path, num_nodes_explored

def breadth_first_search_New(maze, start, end):
    """
    Performs the breadth first search on the maze specified

    Args:
        maze: The maze read from the file and converted to the binary format
        start: The starting coordinates of the ceiling starting node
        end: The end coordinates on the floor of the maze

    Returns:
        shortest_path: An array of the coordinates as a set for the shortest 
                       path found by the algorithm
        num_nodes_explored: The number of nodes the algorithm had to explore 
                            before finding the end node
    
    """
    ROW, COL = len(maze), len(maze[0])

    def is_valid(row, col):
        return 0 <= row < ROW and 0 <= col < COL and maze[row][col] == 1

    def BFS(row, col):
        q = []
        q.append((row, col, 0, [(row, col)]))
        visited = [[False for _ in range(COL)] for _ in range(ROW)]
        visited[row][col] = True
        nodes_explored = 0
        path = []

        while q:
            curr_row, curr_col, dist, curr_path = q.pop(0)
            nodes_explored += 1

            if (curr_row, curr_col) == (end[0], end[1]):
                path = curr_path
                break

            if is_valid(curr_row + 1, curr_col) and not visited[curr_row + 1][curr_col]:
                q.append((curr_row + 1, curr_col, dist + 1, curr_path + [(curr_row + 1, curr_col)]))
                visited[curr_row + 1][curr_col] = True
            if is_valid(curr_row - 1, curr_col) and not visited[curr_row - 1][curr_col]:
                q.append((curr_row - 1, curr_col, dist + 1, curr_path + [(curr_row - 1, curr_col)]))
                visited[curr_row - 1][curr_col] = True
            if is_valid(curr_row, curr_col + 1) and not visited[curr_row][curr_col + 1]:
                q.append((curr_row, curr_col + 1, dist + 1, curr_path + [(curr_row, curr_col + 1)]))
                visited[curr_row][curr_col + 1] = True
            if is_valid(curr_row, curr_col - 1) and not visited[curr_row][curr_col - 1]:
                q.append((curr_row, curr_col - 1, dist + 1, curr_path + [(curr_row, curr_col - 1)]))
                visited[curr_row][curr_col - 1] = True

        return path, nodes_explored

    shortest_path, num_nodes_explored = BFS(start[0], start[1])
    return shortest_path, num_nodes_explored

from queue import Queue

def breadth_first_search(maze, start, end):
    # Initialize queue, visited set, and parent dictionary
    queue = Queue()
    visited = set()
    parent = {}
    
    # Add start node to queue and visited set
    queue.put(start)
    visited.add(start)
    
    # Loop until queue is empty or end node is found
    while not queue.empty():
        # Get next node from queue
        current_node = queue.get()
        
        # Check if end node is reached
        if current_node == end:
            # Reconstruct path from parent dictionary
            path = []
            while current_node != start:
                path.append(current_node)
                current_node = parent[current_node]
            path.append(start)
            path.reverse()
            return path, len(visited)
        
        # Check neighbors of current node
        neighbors = get_neighbors(maze, current_node)
        for neighbor in neighbors:
            if neighbor not in visited:
                # Add neighbor to queue and visited set, and set parent
                queue.put(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current_node
    
    # End node not found
    return [], len(visited)

def get_neighbors(maze, node):
    # Get neighbors of a node in the maze
    neighbors = []
    row, col = node
    if row > 0 and maze[row-1][col] == 1:
        neighbors.append((row-1, col))
    if row < len(maze)-1 and maze[row+1][col] == 1:
        neighbors.append((row+1, col))
    if col > 0 and maze[row][col-1] == 1:
        neighbors.append((row, col-1))
    if col < len(maze[0])-1 and maze[row][col+1] == 1:
        neighbors.append((row, col+1))
    return neighbors


def main():
    # Change to user input
    filename  = "maze-Medium/maze-Large.txt" #= input("Enter the Relative Path of the maze file: ")
    
    maze = maze_to_array(filename)
    start, goal = maze_find_states(maze)
   
    start_time = time.time()
    path, nodes_explored = breadth_first_search_New(maze, start, goal)
    end_time = time.time()

    #print("Nodes explored: ", str(nodes_explored))
    print("Time of execution: ", str(end_time - start_time) , " seconds")

    if path is None:
        print("No path is possible for the start and goal states entered")
    else:
        print("Number of steps in the path: ", len(path))
        print("The number of nodes explored: ", nodes_explored)
        #print(path)

if __name__ == "__main__":
    main()

