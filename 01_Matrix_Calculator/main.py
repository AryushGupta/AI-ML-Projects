from matrix_operation import add_matrix , sub_matrix

ls = list(map(int,input("Matrix elements : ").split()))
matrix = []

# Aim - to form a 2-d matrix from a given 1-d list of integers
row = []
for i in range(0,9,3):
  for j in range(i,i+3):
    row.append(ls[j])
  matrix.append(row)
  row = []