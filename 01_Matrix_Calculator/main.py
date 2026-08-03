from matrix_operation import add_matrix , sub_matrix , mult_matrix , mat_transpose , scal_mult_mat

print("Give two 3X3 matrix")
mat1 = []
mat2 = []

ls1 = list(map(int,input("Matrix elements : ").split()))  
row = []
for i in range(0,9,3):
  for j in range(i,i+3):
    row.append(ls1[j])
  mat1.append(row)
  row = []

ls2 = list(map(int,input("Matrix elements : ").split()))
row = []
for i in range(0,9,3):
  for j in range(i,i+3):
    row.append(ls2[j])
  mat2.append(row)
  row = []

print(mat1)
print(mat2)