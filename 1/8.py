def isSubstring(s1, s2):
  return s1 in s2

def is_rotation (s1, s2):
  return isSubstring(s1, s2 + s2)

s1 = raw_input()
s2 = raw_input()

if is_rotation(s1, s2):
  print "Is a rotation"
else:
  print "Is not a rotation"