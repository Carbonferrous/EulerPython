fileInput = open("p081_matrix.txt")
matrix = [[int(i) for i in x.split(',')] for x in fileInput.read().split("\n")]
fileInput.close()
for j in range(78, -1, -1):
    matrix[79][j] = matrix[79][j] + matrix[79][j+1]
for i in range(78, -1, -1):
    matrix[i][79] = matrix[i][79] + matrix[i + 1][79]
for i in range(78, -1, -1):
    for j in range(78, -1, -1):
        matrix[i][j] = matrix[i][j] + min(matrix[i][j + 1], matrix[i + 1][j])
print(matrix[0][0])
