from matrix_operation import add_matrix , sub_matrix , mult_matrix , mat_transpose , scal_mult_mat
from determinant import determinant

# print("Give two 3X3 matrix")
# mat1 = []
# mat2 = []

# ls1 = list(map(int,input("Matrix elements : ").split()))  
# row = []
# for i in range(0,9,3):
#   for j in range(i,i+3):
#     row.append(ls1[j])
#   mat1.append(row)
#   row = []

# ls2 = list(map(int,input("Matrix elements : ").split()))
# row = []
# for i in range(0,9,3):
#   for j in range(i,i+3):
#     row.append(ls2[j])
#   mat2.append(row)
#   row = []

# print(mat1)
# print(mat2)

# for testing
mat = [[1,2,3],[4,5,6],[7,8,9]]

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
    print(result)
    print(mat[i][j])

    # wrong result because of + - +