def snakePattern(self, matrix): 
        result = []
        n = len(matrix)  # Assuming the matrix is square (N x N)
        for i in range(n):
            if i % 2 == 0:
                for j in range(n):
                    result.append(matrix[i][j])
            else:
                for j in range(n - 1, -1, -1):
                    result.append(matrix[i][j])

        return result
