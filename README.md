# Maze Solver

Maze solver is used to connect start and end point for shortest path.

## Getting Started

These instructions will describe step by step process to run the program in your local machine.


## Prerequisite

```
Python 3.x
```

## Running the program
* To run this program from command prompt use following command:
```
python mazesolver.py -i inputfile -o outputfile
```
* Note: We must require **inputfile'** in CWD (current working directory) with proper input in it.

## Need
To find paths between two location of the matrix (maze), the algorithm can detect when there is no path between the source and destination.

## Program description
I used adjacency matrix to store the input which is present in 'inputfile'.
I created one function named 'create_matrix_file' in which matrix present in inputfile is read once. 
Function 'maze_solver' applies modified BFS to this matrix and creates a list of visited elements wrt their indices. 'visited' list consists required path of maze.
'write_maze_matrix' function converts 'visited' list into a matrix which then stored in 'outputfile'.
If path doesn't exist then 'outputfile' consists -1.

## Built with
[Python](https://www.python.org/) - Language used to build this program.

## Version
* Current version - 0.01

## Git repo
* [link](https://github.com/chaitali-maske-au6/Maze-solver-project.git)
## Author
* **Chaitali Barde**