string = raw_input()
arr = list(string)
l = len(arr)
mid = l / 2
for i in range(mid):
  arr[i], arr[l - i - 1] = arr[l - i -1], arr[i]
print ''.join(arr) 