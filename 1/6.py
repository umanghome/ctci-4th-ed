def rotate90CCW (matrix):
  _matrix = []
  for i in range(len(matrix)):
    _matrix.append([])
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      _matrix[j].append(matrix[i][j])
  _matrix.reverse()
  return _matrix

def rotate90CW (matrix):
  _matrix = []
  for i in range(len(matrix)):
    _matrix.append([])
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      _matrix[j].append(matrix[i][j])
    _matrix[i].reverse()
  return _matrix


def print_matrix (matrix):
  for m in matrix:
    for i in range(len(m)):
      print "%d\t" % m[i],
    print "\n",

n = int(raw_input())
matrix = []
for i in range(n):
  s = raw_input()
  arr = s.split(' ')
  for j in range(len(arr)):
    arr[j] = int(arr[j])
  matrix.append(arr)
print "Original photo:"
print_matrix(matrix)
print "\nRotated photo (CCW):"
print_matrix(rotate90CCW(matrix))
print "\nRotated photo (CW):"
print_matrix(rotate90CW(matrix))