# Addition function
def add_matrix(mat1 : list[list[int]] , mat2 : list[list[int]]) -> list[list[int]]:
  rows = len(mat1)
  columns = len(mat1[0])

  result = []
  for i in range(rows):
    row = []
    for j in range(columns):
      row.append(mat1[i][j] + mat2[i][j])
    result.append(row)

  return result

# Subtraction function
def sub_matrix(mat1 : list[list[int]] , mat2 : list[list[int]]) -> list[list[int]]:
  rows = len(mat1)
  columns = len(mat1[0])

  result = []

  for i in range(rows):
    row = []
    for j in range(columns):
      row.append(mat1[i][j] - mat2[i][j])
    result.append(row)
  return result

# Multiplication function
def mult_matrix(mat1 : list[list[int]] , mat2 : list[list[int]]) -> list[list[int]]:
  rows = len(mat1)
  cols = len(mat1[0])
  result = []

  for i in range(rows):
    new_row = []
    for j in range(cols):
      new_element = 0
      for k in range(cols):
        new_element += mat1[i][k]*mat2[k][j]
      new_row.append(new_element)
    result.append(new_row)

  return result

# Matrix Transpose
def mat_transpose(mat : list[list[int]]) -> list[list[int]]:
  for i in range(2):
    for j in range(1,3):
      mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]
  return mat

# Scalar Multiplication
def scal_mult_mat(mat : list[list[int]] , k : int) -> list[list[int]]:
  for i in range(3):
    for j in range(3):
      mat[i][j] *= k
  return mat