"""
This module contains a collection of functions performing the depth-first-search
algorithm on any given maze.

Functions:
- maze_find_states: Finds the coordinates of the start and end nodes in the maze
- maze_to_array: Converts the maze into a binary representation
- dfs: Performs the depth-first-search on the maze
- main: The logical order and terminal I/O of the program

Author: Jude Wallace
Date: March 12, 2023
"""
#Imports
import time

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
        filename: The relative path to the .txt of the maze

    Returns:
        convert_to_binary(arr): The maze read as a binary representation
    """
    # Open the file and strip any unnecessary characters
    with open(filename, "r") as file:
        contents = file.read().splitlines()
        contents = [list(row.replace(" ", "")) for row in contents if row.strip()]
   
    def convert_to_binary(arr):
        """
        Converts the maze into a the correct format for the program

        Args:
            arr: The array of the contents read from the file

        Returns:
            converted: The file contents converted to the correct format of 
                       a binary representation where a 0 is a wall and a 1
                       is a path node
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

def dfs(maze, start, end):
    """Perform depth-first search to find a path through a maze.

    Args:
        maze: A 2D list representing the maze, where 0's represent walls and 1's represent open paths.
        start: A tuple representing the starting position in the maze.
        end: A tuple representing the end position in the maze.

    Returns:
        path: A tuple of coordinates of the path nodes.
        len(visited): The number of nodes the algorithm explored.
        None
        -1
    """
    # Check if start or end points are walls
    if maze[start[0]][start[1]] == 0 or maze[end[0]][end[1]] == 0:
        return None, -1

    # Initialize stack, visited set, and path list
    stack = [(start, [start])]
    visited = set()
    path = []

    # Define the order of exploration for neighbors
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Loop until stack is empty
    while stack:
        node, path = stack.pop()

        if node == end:
            return path, len(visited)

        if node in visited:
            continue

        # Add node to visited set
        visited.add(node)

        # Get neighbors of current node in the specified order
        for direction in directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])

            # Check if neighbor is valid
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == 1:
                # Add neighbor to stack with updated path
                stack.append((neighbor, path + [neighbor]))

    # If end point is not found, return -1 and None
    return None, -1

def main():
    """
    Runs the main logic of the program
    """
    filename  = input("Enter the Relative Path of the maze file: ")

    # Convert the maze
    maze = maze_to_array(filename)
    
    start, goal = maze_find_states(maze)
    # Time the algorithm as it is performed on the maze
    start_time = time.time()
    path, nodes_explored = dfs(maze, start, goal)
    end_time = time.time()

    print("Nodes explored: ", str(nodes_explored))
    print("Time of execution: ", str(end_time - start_time) , " seconds")

    if path is None:
        print("No path is possible for the start and goal states entered")
    else:
        print("Number of steps in the path: ", str(len(path)))
        print(path)

if __name__ == "__main__":
    main()
