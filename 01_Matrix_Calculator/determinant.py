def determinant(mat : list[list[int]]) -> int :
  # for 3X3 matrix
  result = 0

  for i in range(1):
    row = [1,2]
    for j in range(3):
      if(j == 0):
        col = [1,2]
      elif(j == 1):
        col = [0,2]
      else:
        col = [0,1]

      result += mat[i][j]*((mat[row[0]][col[0]] * mat[row[1]][col[1]]) - (mat[row[0]][col[1]] * mat[row[1]][col[0]]))

  return result