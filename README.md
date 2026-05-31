# Maze Solver using A* Search

This repository contains the Week 1 project for the Syntecxhub Internship program. The goal of this project is to implement an intelligent pathfinding algorithm to navigate a grid-based maze.

## Project Description

The project implements the **A* (A-Star) Search Algorithm** to find the shortest possible path from a starting node to a goal node within a 2D maze. The maze is represented as a grid where `0` denotes walkable paths and `1` denotes walls/obstacles.

### Approach & Implementation Details

1. **Maze Representation**: 
   - The grid is modeled as a 2D array.
   - Each cell in the grid is treated as a discrete `Node` that tracks its coordinates, its parent node, and its cost values for the search.

2. **A* Search Algorithm**:
   - Uses a priority queue (`heapq`) to evaluate the most promising nodes first, optimizing search time.
   - **Heuristic**: The algorithm uses the **Manhattan Distance** heuristic. Since movement is restricted to four directions (Up, Down, Left, Right), Manhattan Distance perfectly estimates the cost to reach the goal.
   - **Cost Function ($f = g + h$)**: 
     - $g$: The exact cost from the starting node to the current node.
     - $h$: The estimated Manhattan distance from the current node to the goal.
     - $f$: The total estimated cost of the path through the current node.

3. **Handling Edge Cases**:
   - The algorithm gracefully handles unreachable goals (e.g., when the goal is completely walled off) by returning `None` when the open list is exhausted.
   - Prevents backtracking and infinite loops by utilizing a `closed_list` to keep track of already-visited nodes.

4. **Visualization**:
   - A custom `print_maze` function displays the maze in the console. 
   - It marks walls as `#`, the starting point as `S`, the goal as `E`, and the final computed shortest path as `*`.

## How to Run

Simply execute the python script in your terminal:
```bash
python maze_solver.py
```
The script will print the initial maze structure and the final solved maze with the optimal path plotted.
