class gaussJordanClass:
    
    matrix = [[]]
    
    def __init__(self, matrix): 
        self.matrix = matrix


    def getSoluion (self):
        return self.gauss_jordann(self.matrix)
    
    def gauss_jordann(m):
        (h, w) = (len(m), len(m[0]))
        for y in range(0,h):
            maxrow = y
            for y2 in range(y+1, h):
                if abs(m[y2][y]) > abs(m[maxrow][y]):
                    maxrow = y2
            (m[y], m[maxrow]) = (m[maxrow], m[y])
            for y2 in range(y+1, h):       
                c = m[y2][y] / m[y][y]
                for x in range(y, w):
                    m[y2][x] -= m[y][x] * c
        for y in range(h-1, 0-1, -1): 
            c = m[y][y]
            for y2 in range(0,y):
                for x in range(w-1, y-1, -1):
                    m[y2][x] -= m[y][x] * m[y2][y] / c
            m[y][y] /= c
            for x in range(h, w):             
                m[y][x] /= c
        sol = []
        for i in range(0, h):
            sol.append(m[i][w-1])
        return sol
