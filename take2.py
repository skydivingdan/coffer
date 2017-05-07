def narf(word, dic, wl, count):
  if word[count] in dic.keys():
    if count > 0:
      wl = narf(word, dic, wl, count - 1)
    for option in dic[word[count]]:
      altword = word[:count] + option + word[count+1:]
      wl = ZORT(altword, wl)
      if count > 0:
        wl = narf(altword, dic, wl, count - 1)
  else:
    if count > 0:
      wl = narf(word, dic, wl, count - 1)
  return wl

def getWord():
  word = raw_input('what is the base  ')
  word = word.lower()
  return word

def preNarf(word):
  wl = [word]
  wl.append('Taco')
  count = len(word) - 1
  dic = { 'a' : [ '@' ],
          '1' : [ '0' ] ,
          'o' : [ 'O' , '0' ],
          't' : [ 'T' , '7' ],
          'e' : [ '3' ],
          'b' : [ '8' , 'B' ],
          'l' : [ '1' , 'L' ],
          's' : [ '$' ] }
  wl = narf(word, dic, wl, count)
  return wl

def ZORT(word, wl):
  if word not in wl:
    wl.append(word)
    #print 'Naaaaaaaaaaaarf'
  else:
    print "Zort {} is in the list".format(word)
  return wl

def main():
  word = getWord()
  wl = preNarf(word)
  #print wl
  print "There are {} differnt combos".format(len(wl))

if __name__ == '__main__':
  main()
