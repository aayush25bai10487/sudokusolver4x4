# Problem Statement

The objective of this project is to develop an efficient command-line application that can solve Sudoku puzzles of a specific 4x4 format with 2x2 sub-grids. The application must accept user input for an unsolved puzzle (represented as a 2D matrix where zeros indicate empty cells) and output the unique, logically derived solution. The solver needs to employ algorithmic strategies, specifically constraint satisfaction and backtracking, to find the correct configuration that adheres to standard Sudoku rules: each row, column, and 2x2 sub-grid must contain the numbers 1 through 4 exactly once.

# Scope of the Project

The scope of this project is a minimal viable product (MVP) focused purely on the core solving logic for a fixed 4x4 board size using the provided Python and NumPy implementation.

-  In Scope:
   - Accepting user input via the console for a 4x4 grid.
   - Implementing logic to check the validity of moves within rows, columns, and 2x2 boxes.
   - Utilizing a hybrid solving approach combining deterministic constraint propagation (filling single-possibility cells) and recursive backtracking.
   - Outputting the solved 4x4 matrix to the console.
  
- Out-of-Scope:
   - Graphical User Interface (GUI).
   - Handling or validating user input for standard 9x9 Sudoku boards.
   - Error handling for invalid or unsolvable input puzzles.
   - Generating new Sudoku puzzles.

# Target Users

The primary target users for this application are:
- Hobbyist Programmers/Students: Individuals interested in studying or implementing basic artificial intelligence and backtracking algorithms for constraint satisfaction problems.
- Developers: Those who need a foundational, functional Sudoku solver implementation in Python that can be integrated into larger projects or expanded upon (e.g., as the logic layer for a web-based Sudoku game).

# High-Level Features

- Interactive Console Input: Allows users to define their 4x4 puzzle matrix dynamically at runtime.
- NumPy Integration: Leverages the numpy library for efficient array manipulation and matrix slicing.
- Hybrid Solving Algorithm: Combines two methods for efficiency:
  - Constraint Propagation: Automatically fills cells where only one possible number is valid.
  - Backtracking Recursion: Systematically explores potential solutions when deterministic moves are exhausted.
- Clear Output: Presents the final solved matrix in a readable 2D format on the console.


  
