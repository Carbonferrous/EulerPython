fileInput = open("p081_matrix.txt")
matrix = [[int(i) for i in x.split(',')] for x in fileInput.read().split("\n")]
fileInput.close()
print(matrix)
