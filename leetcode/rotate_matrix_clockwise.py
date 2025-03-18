class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        # transpose using nested loops
        for row in range(len(matrix)):
            for column in range(row+1, len(matrix)):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
