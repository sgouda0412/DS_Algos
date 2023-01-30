from typing import List
def setZeroes(matrix: List[List[int]]) -> List[List[int]]:
    m, n = len(matrix), len(matrix[0])
    row, col = set(), set()
        
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
        
    for i in range(m):
        for j in range(n):
            if i in row or j in col:
                matrix[i][j] = 0
    return matrix


if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    setZeroes(matrix)
