string = raw_input()
arr = list(string)
i = 0
while i < len(arr):
  c = arr[i]
  j = i + 1
  while j < len(arr):
    if arr[j] is c:
      arr.pop(j)
    j = j + 1
  i = i + 1
print ''.join(arr)