"""
This module contains a collection of functions performing the depth-first-search
algorithm on any given maze.

Functions:
- maze_find_states: Finds the coordinates of the start and end nodes in the maze
- maze_to_array: Converts the maze into a binary representation
- breadth_first_search: Performs the breadth-first-search on the maze
- get_neighbours: Get the neighbouring nodes of the current node being checked
- main: The logical order and terminal I/O of the program

Author: Jude Wallace
Date: March 12, 2023
"""
# Imports required for the program
import time
from queue import Queue


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


def breadth_first_search(maze, start, end):
    """
    Performs the breadth first search on the maze specified

    Args:
        maze: The maze read from the file and converted to the binary format
        start: The starting coordinates of the ceiling starting node
        end: The end coordinates on the floor of the maze

    Returns:
        path: An array of the coordinates as a set for the shortest 
                       path found by the algorithm
        len(visited): The number of nodes the algorithm had to explore 
                      before finding the end node
    
    """
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
        neighbours = get_neighbours(maze, current_node)
        for neighbour in neighbours:
            if neighbour not in visited:
                # Add neighbor to queue and visited set, and set parent
                queue.put(neighbour)
                visited.add(neighbour)
                parent[neighbour] = current_node
    
    # End node not found
    return [], len(visited)

def get_neighbours(maze, node):
    """
    Returns a list of neighboring nodes in the maze that can be reached from the given 
    node.

    Args:
      maze: A 2D list representing the maze, where 1 represents an open path and 0 
      represents a wall.
      node: A tuple representing the (row, col) position of the node in the maze.

    Returns:
      neighbors: A list of tuples representing the (row, col) positions of neighboring 
      nodes that can be reached from the given node.
    """
    # Get neighbors of a node in the maze
    neighbours = []
    row, col = node
    if row > 0 and maze[row-1][col] == 1:
        neighbours.append((row-1, col))
    if row < len(maze)-1 and maze[row+1][col] == 1:
        neighbours.append((row+1, col))
    if col > 0 and maze[row][col-1] == 1:
        neighbours.append((row, col-1))
    if col < len(maze[0])-1 and maze[row][col+1] == 1:
        neighbours.append((row, col+1))
    return neighbours


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
    path, nodes_explored = breadth_first_search(maze, start, goal)
    end_time = time.time()

    print("Time of execution: ", str(end_time - start_time) , " seconds")

    if path is None:
        print("No path is possible for the start and goal states entered")
    else:
        print("Number of steps in the path: ", len(path))
        print("The number of nodes explored: ", nodes_explored)
        print(path)

if __name__ == "__main__":
    main()

