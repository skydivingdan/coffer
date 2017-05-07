import random
import math
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

numtest = int(raw_input('How many trials? ') )

for i in range( 1, numtest ):
  p = random.randint(1,6)
  if p == 1:
    a += 1
  elif p == 2:
    b += 1
  elif p == 3:
    c += 1
  elif p == 4:
    d += 1
  elif p == 5:
    e += 1
  elif p == 6:
    f += 1

print "Rolls complete"

print float(a)/float(numtest)*100, "is the prob for 1"
print float(b)/float(numtest)*100, "is the prob for 2"
print float(c)/float(numtest)*100, "is the prob for 3"
print float(d)/float(numtest)*100, "is the prob for 4"
print float(e)/float(numtest)*100, "is the prob for 5"
print float(f)/float(numtest)*100, "is the prob for 6"
