def gg(matrix):
    n = len(matrix)
    
    work_matrix = [row[:] for row in matrix]
    
    for k in range(n):
        pivot = work_matrix[k][k]
        if pivot == 0:
            raise None

        for j in range(k, 2*n):
            work_matrix[k][j] /= pivot

        for i in range(k+1, n):
            factor = work_matrix[i][k]
            for j in range(k, 2*n):
                work_matrix[i][j] -= factor * work_matrix[k][j]
    
    for k in range(n-1, -1, -1):
        for i in range(k):
            factor = work_matrix[i][k]
            for j in range(2*n):
                work_matrix[i][j] -= factor * work_matrix[k][j]
    
    return work_matrix

input_matrix = [
    [1.02, -0.25, -0.15, 1, 0, 0],
    [-0.41, 1.13, -0.15, 0, 1, 0],
    [-0.25, -0.14, 1.21, 0, 0, 1],
]

input_matrix = [list(map(float, row)) for row in input_matrix]

matrices = []
for i in range(3):
    current_matrix = [row[:] for row in input_matrix]
    for row in current_matrix:
        row[3], row[3+i] = row[3+i], row[3]
    result = gg(current_matrix)
    matrices.append(result)

for i, sol in enumerate(matrices):
    for s in sol:
        print(*[f"{x:>7.4f}" for x in s])
        
    print()
    
#  1.0000 -0.2451 -0.1471  0.9804  0.0000  0.0000
#  0.0000  0.9111 -0.1861  0.3557  0.8850  0.0000
#  0.0000 -0.0179  0.9387  0.2617  0.1472  0.8264

#  1.0000 -0.2451 -0.1471  0.9804  0.0000  0.0000
#  0.0000  0.9111 -0.1861  0.3557  0.8850  0.0000
#  0.0000 -0.0179  0.9387  0.2617  0.1472  0.8264

#  1.0000 -0.2451 -0.1471  0.9804  0.0000  0.0000
#  0.0000  0.9111 -0.1861  0.3557  0.8850  0.0000
#  0.0000 -0.0179  0.9387  0.2617  0.1472  0.8264