# PythonTreasureHunt
python practice from something i did in Java a while back. 

PA1: Backtracking Treasure Hunt


Backtracking Treasure Hunt

Objectives

Demonstrate what you've learned programming in Python to solve one of the earlier labs in CS 2440.
Read data from a text file and populate an appropriate data structure in Python.
Implement a recursive depth-first-search algorithm to solve the game and print the solution in Python.
Introduction

Recall the 2440 lab in which you implemented a game called Treasure Hunt. (You may have implemented the Goblins puzzle or the Maze Game instead; the backtracking strategy is the same.)  The goal of this game is to find a path from the center of an 11 x 11 game board to any one of the corners.  Each square of the board contains an integer that specifies the number of spaces up, down, left, or right that must be used to move from that cell to another cell. It is often difficult to win the game because paths to a corner can be quite complicated. For example, a solution to this board is shown below the board.

0 8 6 5 7 7 2 4 6 2 0 
8 3 9 6 3 8 3 9 5 6 4 
4 9 5 3 6 9 9 4 6 8 9 
6 8 3 9 7 3 4 4 2 5 4 
2 5 8 3 4 9 3 2 3 9 1 
4 2 4 6 9 3 5 8 3 9 2 
9 5 6 2 6 7 9 2 6 8 2 
6 3 8 4 7 4 8 4 9 9 6 
5 8 5 4 4 7 5 9 4 8 4 
2 7 4 2 5 7 2 9 2 8 6 
0 4 9 4 4 2 7 5 3 1 0

right up down up up left right down left up down right up right left up right down up down down right

Understanding the Recursive Approach

Imagine that you are asked, "Is there a path to a corner from the center ([5][5]) of the above puzzle?"

Your answer is, "There is a solution from [5][5] 
only if there is a solution from either [2][5] 
or from [5][8] or from [8][5] or from [5][2]." Those 
cells are each 3 steps away from [5][5] and there is a 3 at [5][5].

So then you are asked, "Is there a solution from [2][5]?" 
And your answer is, "There cannot be a solution from [2][5] 
because there is a 9 at [2][5] and all of the cells that are 
9 steps from [2][5] are off the board."

Your inquisitor continues, "So what about your second possibility? 
Is there a solution from [5][8]?" Your answer is, "There is a 
solution from [5][8] only if there is a solution from [2][8] or from 
[8][8]. We can't consider [5][11] because there is no such cell on 
the board, and we've already been to [5][5]."

This process goes on and on until you are asked, "Is there a solution 
from [10][10]?" and you answer, "There is, because [10][10] is a corner."

Backtracking

Backtracking is a recursive technique that makes a choice at a certain point in 
the search but, if it gets stuck, it returns to the last place that a choice was 
made and tries a different choice instead.  Look at the following general backtracking 
algorithm pseudocode.  It can be used to solve LOTS of problems.  Your book suggested 
it for finding a path through a maze. The currentState parameter refers to whatever 
values are needed to describe where one currently is in the search.

algorithm backtrack(currentState)
{
				if (currentState is the solution)
				{
								return solution
				}
				else
				{         
								for (each possibleState reachable from here)
								{
												isSuccess = backtrack (possibleState)
																if (isSuccess)
																{
																				return isSuccess;
																}            
								}
								return failure;   // failure might be represented by a null value
				} 
}
For your backtracking treasure hunting program, you might represent the currentState as 
three parameters: the current row and column indexes, and a list containing the moves taken
so far to get there. Also, the above pseudocode makes it appear that the backtrack metho
d returns a boolean but it doesn't have to. We choose to return a String. It will be the path t
aken so far unless we have gotten stuck. In that case we will return null.

Your instructors wrote a recursive solution for the Treasure Hunt problem (it wasn’t much code), and added print st
atements to show how the backtracking was proceeding. You do not have to include such print statements unless you n
eed them to help in debugging.  But the statements below the following grid will help you understand the backtracki
ng process on that grid. The indentation level signifies one level of the recursion tree. There is a picture of the
full recursion tree after the print statements, but you should realize that the algorithm only generates enough of 
the recursion tree to find a solution. It stops once a solution is found.

0 0 0 0 0 0 0 3 0 0 0
0 0 0 0 0 2 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 4 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0

Printout:

Current position: (5, 5, "").

Try moving up 4 spaces.

Current position: (1, 5, "up ").

Try moving up 2 spaces.

Current position: (-1, 5, "up up ").

Moved off board (-1, 5), try again.

Try moving right 2 spaces.

Current position: (1, 7, "up right ").

Try moving up 1 spaces.

Current position: (0, 7, "up right up ").

Try moving up 3 spaces.

Current position: (-3, 7, "up right up up ").

Moved off board (-3, 7), try again.

Try moving right 3 spaces.

Current position: (0, 10, "up right up right ").

Found a solution (0, 10), return it!

Found a solution, return it!

Found a solution, return it!

Found a solution, return it!

Found a solution, return it!

Implementation

One helpful thing to do is to keep track of the squares your algorithm has already visit
ed.  That way you can avoid revisiting a square that is already being tested.  Each time
the backtrack algorithm is called with a row and column, it can mark that row and column
in the "visited" array. And if the backtrack method generates a position to try that has
already been visited, it doesn't try that position.

Submitting

Submit one Python file that reads a file name from the command line and solve the Treasu
re Hunt game by displaying the solution in the console.
