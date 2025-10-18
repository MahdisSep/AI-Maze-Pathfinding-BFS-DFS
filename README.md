# AI Maze Pathfinding Simulation (BFS & DFS)

## 🌟 Project Overview

This project is an **Artificial Intelligence** assignment focused on implementing and visualizing **uninformed search algorithms**. It models a classic problem: guiding an **Agent** from a starting point to a goal within a complex, predefined **Maze Environment**.

The core objective is to demonstrate the differences in behavior and efficiency between **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**, specifically how each explores the state space (the maze) to find the optimal or first valid path. The simulation uses **Pygame** to provide a clear, tile-based visualization of the search process, showing which nodes are explored (the search frontier) and the final solution path.

## ⚙️ Algorithms Implemented

| Algorithm | Type | Data Structure | Key Feature |
| :--- | :--- | :--- | :--- |
| **Breadth-First Search (BFS)** | Uninformed | Queue (`deque`) | Finds the **shortest path** in terms of the number of steps (due to uniform cost per step). |
| **Depth-First Search (DFS)** | Uninformed | Stack | Explores as far as possible along each branch before backtracking. **Guaranteed to find a solution** but not necessarily the shortest. |

## 🚀 Key Features

  * **Real-Time Visualization:** Utilizes **Pygame** to visually represent the 13x13 maze, displaying:
      * Start and Goal locations.
      * Blocked cells (walls).
      * **Explored Nodes** (Search Frontier).
      * The **Final Solution Path**.
  * **Modular Design:** Separates core components into dedicated classes/files: `Agent`, `Environment`, and `Tile`.
  * **Agent-Environment Paradigm:** Follows a standard AI approach where the `Agent.py` perceives the state from `Environment.py` and decides on the next action (move).
  * **Maze Loading:** Loads a predefined maze configuration from a NumPy file (`Maze.npy`), allowing for easy changes to the problem space.

## 🛠️ Technology Stack

  * **Language:** Python
  * **Simulation/Visualization:** Pygame
  * **Data Structures:** NumPy (`Maze.npy`), Python `collections.deque` (for BFS).
  * **Concepts:** State-Space Search, Graph Traversal, Informed vs. Uninformed Search.

## 📁 Project Structure

| File | Role |
| :--- | :--- |
| `main.py` | Main execution file; initializes Pygame, the Board, and the Agent, and runs the game loop. |
| `Agent.py` | Contains the `Agent` class and the implementation of the **BFS** and **DFS** search logic. |
| `Environment.py` | Defines the `Board` class, which manages the maze grid, loads the map data, and handles visualization updates. |
| `tile.py` | Defines the `Tile` class, representing a single cell in the maze with properties (blocked, start, goal, color). |
| `params.py` | Stores global constants for the simulation (e.g., `rows`, `cols`, `width`, `height`). |
| `colors.py` | Defines RGB color constants used for visualization. |
| `Maze.npy` | The binary file containing the 13x13 maze structure (0 for wall, 1 for path). |

## 💻 How to Run the Project

1.  **Prerequisites:** Ensure you have **Python 3** and the necessary libraries installed:
    ```bash
    pip install pygame numpy
    ```
2.  **Execution:** Run the main application file from your terminal:
    ```bash
    python main.py
    ```
3.  **Simulation:** The Pygame window will open, displaying the maze. The search agent will typically execute the defined algorithm (e.g., BFS or DFS, depending on which one is uncommented in `main.py`) to find and display the path from the start tile to the goal tile.