class gaussEliminationClass:
    
    matrix = [[]]
    
    def __init__(self, matrix): 
        self.matrix = matrix


    def getSoluion (self):
        return self.gauss(self.matrix)

    def gauss(A):
        n = len(A)
    
        for i in range(0, n):
            # Pivoting 
            # Search for maximum in this column
            maxEl = abs(A[i][i])
            maxRow = i
            for k in range(i+1, n):
                if abs(A[k][i]) > maxEl:
                    maxEl = abs(A[k][i])
                    maxRow = k
    
            # Swap maximum row with current row (column by column)
            for k in range(i, n+1):
                tmp = A[maxRow][k]
                A[maxRow][k] = A[i][k]
                A[i][k] = tmp
        
            # Make all rows below this one 0 in current column
            for k in range(i+1, n):
                c = -A[k][i]/float(A[i][i])
                for j in range(i, n+1):
                    if i == j:
                        A[k][j] = 0
                    else:
                        A[k][j] += c * A[i][j]
    
        # Back Substitution
        x = [0 for i in range(n)]
        for i in range(n-1, -1, -1):
            x[i] = A[i][n]/A[i][i]
            for k in range(i-1, -1, -1):
                A[k][n] -= A[k][i] * x[i]
        return x
