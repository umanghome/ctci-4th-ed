def matrix_oper (matrix):
  cols = []
  rows = []
  m = len(matrix)
  n = len(matrix[0])
  for i in range(m):
    for j in range(n):
      try:
        v = rows.index(i)
        continue
      except:
        try:
          v = cols.index(j)
          continue
        except:
          if matrix[i][j] == 0:
            rows.append(i)
            cols.append(j)
            matrix[i] = []
            for k in range(n):
              matrix[i].append(0)
            for k in range(m):
              # print_matrix(matrix)
              matrix[k][j] = 0
  return matrix

def print_matrix (matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      print "\t%d" % matrix[i][j],
    print "\n",

m = int(raw_input())
n = int(raw_input())
matrix = []
for i in range(m):
  s = raw_input()
  arr = s.split(' ')
  for j in range(len(arr)):
    arr[j] = int(arr[j])
  matrix.append(arr)

print_matrix(matrix_oper(matrix))