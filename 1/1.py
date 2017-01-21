string = raw_input()
uniq = True
for c in string:
  if string.count(c) > 1:
    uniq = False
    break
if uniq:
  print "Unique"
else:
  print "Not unique"