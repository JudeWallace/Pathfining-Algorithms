"""
This module contains a collection of functions performing the A* algorithm on 
any given maze.

Functions:
- maze_find_states: Finds the coordinates of the start and end nodes in the maze
- maze_to_array: Converts the maze into a binary representation
- heuristic: Calculates the manhattan distance between a, b 
- astar: Performs the A* algorithm on the maze
- main: The logical order and terminal I/O of the program

Author: Jude Wallace
Date: March 12, 2023
"""
#Imports
import heapq
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

def heuristic(a, b):
    """
    Calculates the Manhattan distance between two points a and b.

    Args:
        a: A tuple containing the x and y coordinates of the first point.
        b: A tuple containing the x and y coordinates of the second point.

    Returns:
        The Manhattan distance between points a and b.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(array, start, goal):
    """
    Finds the shortest path from start to goal in the given 2D array using the A* algorithm.

    Args:
        array: A list of lists representing the 2D array. Walls are represented by 0, and
               all other values are considered passable terrain.
        start: A tuple containing the x and y coordinates of the starting position.
        goal: A tuple containing the x and y coordinates of the goal position.

    Returns:
        date[::-1]: A list of tuples representing the shortest path from start to goal. 
                    If no path exists, this will be None.
        num_visited: An integer representing the number of nodes visited during the search.
    """
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []
    num_visited = 0

    heapq.heappush(oheap, (fscore[start], start))

    # Loop until the priority queue is empty
    while oheap:
        current = heapq.heappop(oheap)[1]
        num_visited += 1

        # If the goal has been reached, backtrack the optimal path and return it
        if current == goal:
            data = [current]
            while current in came_from:
                current = came_from[current]
                data.append(current)
            return data[::-1], num_visited

        close_set.add(current)
        # Loop over the neighbors of the current cell
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            # Compute the tentative g-score for the neighbor
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            # Check if the neighbor is within the boundaries of the array and is not a wall
            if 0 <= neighbor[0] < len(array):
                if 0 <= neighbor[1] < len(array[0]):
                    if array[neighbor[0]][neighbor[1]] == 0:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            # Check if the neighbor has already been visited with a lower or equal g-score
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
            
            # Update the g-score, f-score, and path to the neighbor if it has not been visited yet
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return None, num_visited

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
    path, nodes_visited = astar(maze, start, goal)
    end_time = time.time()

    print("Time of execution: ", str(end_time - start_time) , " seconds")

    if path is None:
        print("No path is possible for the start and goal states entered")
    else:
        print("Number of steps in the path: ", len(path))
        print("The number of nodes explored: ", nodes_visited)
        print(path)

if __name__ == "__main__":
    main()
