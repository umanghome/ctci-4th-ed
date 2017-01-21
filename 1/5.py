def replaceSpace (str):
  arr = list(str)
  for i in range(len(arr)):
    if arr[i] == ' ':
      arr[i] = '%20'
  return ''.join(arr)

a = raw_input()
print replaceSpace(a)