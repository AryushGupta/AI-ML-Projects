mat = [[1,2,3],[4,5,6],[7,8,9]]

# Matrix Transpose
for i in range(0,3):
  for j in range(0,3):
    element = mat[i][j]
    mat[i][j] = mat[j][i]
    mat[j][i] = element

print(mat)