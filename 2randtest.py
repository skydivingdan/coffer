import math, random, numpy 

X = int(raw_input('How many numbers '))
Y = int(raw_input('How many trial '))
T = 0
print "\nInto the Rabbit Hole....\n"
result = []
for i in range(1, X+1):
  exec("num{} = 0 ".format(i)) 

for n in range(1,Y+1):
  r = random.randint(1,X)
  exec("num{} += 1".format(r))

for i in range(1,X+1):
  #exec("print \"num{}'s prob is \", float(num{})/float(Y)*100".format(i,i))
  exec("result.append(float(num{})/float(Y)*100)".format(i))
  exec("T = T + float(num{})/float(Y)".format(i))
  

print T
print "Mean  :", numpy.mean(result)
print "Min   :", numpy.amin(result)
print "Max   :", numpy.amax(result)
print "Stdev :", numpy.std(result)
