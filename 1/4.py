def anagrams (a, b):
  a = list(a)
  b = list(b)
  a.sort()
  b.sort()
  return a == b

a = raw_input()
b = raw_input()
if anagrams(a, b):
  print "Anagrams"
else:
  print "Not anagrams"