
You're given a two-dimensional array (a matrix) of distinct integers and a target integer. Each row in the matrix is sorted, and each column is also sorted; the matrix doesn't necessarily have the same height and width.


Write a function that returns an array of the row and column indices of the target integer if it's contained in the matrix, otherwise
**[-1, -1]**.

Example:<br>
Input:<br>
array = [<br>
  [1, 4, 7, 12, 15, 1000], <br>
  [2, 5, 19, 31, 32, 1001], <br>
  [3, 8, 24, 33, 35, 1002],<br>
  [40, 41, 42, 44, 45, 1003],<br>
  [99, 100, 103, 106, 128, 1004],<br>
]<br>
Output:<br>
[3, 3]