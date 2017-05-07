

def ask():
  phrase = raw_input("What is the passphrase? >")
  l = len(phrase)
  return phrase, l

def subs(pp, l):
  change = {'a' : '@',
	  'o' : '0',
          'b' : 'B',
          '1' : '0', 
          't' : 'T',
          '0' : '1'}
  #workpp = list(pp)
  c = 0
  count = 1 
  print pp
  for i in pp:
    workpp = list(pp)
    if workpp[c] in change.keys():
      # print workpp[i] 
      workpp[c] = change[workpp[c]]
      print "".join(workpp),"outside"
      count += 1  
      sc = 0
      while sc < c:
        workpp1 = workpp  
        if workpp1[sc] in change.keys():
          workpp1[sc] = change[workpp1[sc]]
          print "".join(workpp1),"inside"
          count += 1 
        else:
          print "pass inside loop"
        sc += 1
    else:
      print "pass outside loop"
    c += 1
  print "DONE BITCH"
  print "there are %d permeiations of this password" % count


def fileOpen():
  f = open('output.list', 'w')
  return f
def fileClose(f):
  close(f)

def subs2(pp, l):
  change = {'a' : '@',
	  'o' : '0',
          'b' : 'B',
          '1' : '0', 
          't' : 'T',
          '0' : '1'}
  wp = list(pp)
  wp2 = wp
  fc = 0
  sc = 0
  wordlist = [] 
  wordlist.append(pp)
  for i in wp:      #flip first ones
    if wp[fc] in change.keys():
      wp[fc] = change[wp[fc]]
      if "".join(wp) in wordlist:
        pass
      else:
        wordlist.append("".join(wp))
    for g in wp:
      if fc == sc:
        pass
      else:
        if wp[sc] in change.keys():
          wp[sc] = change[wp[sc]]
          if "".join(wp) in wordlist:
            pass
          else:
            wordlist.append("".join(wp))
          wp[sc] = change[wp[sc]]
          sc += 1 
        
    fc += 1
    sc = 0
  print len(wordlist)

  print wordlist

def subs3(pp, l, wl, ch, count):
  wl = al(wl, "".join(pp))
  if pp[count] in ch.keys():
    pp[count] = ch[pp[count]]
    wl = al(wl, "".join(pp))
  else:
    pass
  count += 1 
  if count <= l:
    subs3(pp, l, wl, ch, count)
  else:
    pass
  return wl

def subs4(pp, l, wl, ch, count):
  wp = pp
  wl = al(wl, "".join(pp))
  if count < l:
    if wp[count] in ch.keys():
      wp[count] = ch[wp[count]]
      wl = al(wl, "".join(wp)
      wp[count] = pp[count]
  if count == l
    

def al(wl, s):
  if s not in wl:
    wl.append(s)
  else:
    pass
  return(wl)
    
      
#STARTS MAIN
###  Get some variables out of the way... heyheyhey
phrase, sc = ask()
sc = sc - 1 
#subs2(phrase, sc)
wordlist = []
change = {'a' : '@',
	  'o' : '0',
          'b' : 'B',
          '1' : '0', 
          't' : 'T',
          '0' : '1'}
pp = list(phrase)
count = 0 
########################  Into to rabbit hole we go
wordlist = subs3(pp, sc, wordlist, change, count)
print wordlist
print len(wordlist)
