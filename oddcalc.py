bits = float(eval(input('How many bits?   ')))
prob = 1.0
notprob = 1.0
num = 1
while prob < .5 or num == 1:
  #prob = 1 - ((2**bits - num)/(2**bits))
  #print float(((bits-num)/bits)), num, bits
  #prob = 1.0 - float(prob * float(float(bits - num)/float(bits)))
  notprob = notprob * (bits - num)/bits
  print( prob, notprob)
  prob = 1.0 - notprob
  num +=1 

print (num, "number")
print (prob)

