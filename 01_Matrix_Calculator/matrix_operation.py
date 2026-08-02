# Addition function
def add_matrix(mat1,mat2):
  rows = len(mat1)
  columns = len(mat1[1])

  result = []
  for i in range(rows):
    row = []
    for j in range(columns):
      row.append(mat1[i][j] + mat2[i][j])
    result.append(row)

  return result

# Subtraction function
def sub_matrix(mat1,mat2):
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
def mult_matrix(mat1,mat2):
  result = []
  return result