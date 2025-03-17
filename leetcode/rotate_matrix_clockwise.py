class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        j = len(matrix)
        # reverse rows first
        matrix.reverse()
        # transpose matrix with loop
        for row in range(0, j):
            # add empy row at the end
            matrix.append([])
            for column in range(0, j):
                matrix[-1].append(matrix[column][row])

        # delete old rows
        for row in range(0,j):
           del matrix[0]
