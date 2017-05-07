#!/usr/bin/python
zap = 0

def subs(wl, ch):       ###########  wl = wordlist  ch = Changes, pos = position, c,d,f = counters
  for key in ch.keys():
    if key in wl[0]:
      for option in ch[key]:
        c = wl[0].count(key)
        d = 0
        pos = [-1]
        while d <= c:
          pos.append(wl[0].find(key, pos[d]+1))
          d += 1 
        f = 1
        e = len(pos) - 1
        while f < e:
          for itr in wl:
            wl = al(wl, itr[:pos[f]]+itr[pos[f]:].replace(key,option))
            wl = al(wl, itr[:pos[f]]+itr[pos[f]:].replace(option, key))
          f +=1
    else: 
      pass 
  return wl            

def ask():
  phrase = raw_input("What is the root phrase?  ")
  wl = []
  wl.append(phrase)
  return wl

def al(wl, s):
  if s not in wl:
    wl.append(s)
  else:
    print "Zap... {} is in the wl".format(s)
    global zap 
    zap += 1
  return wl

def filefilefile(wl):
  with open('list.txt', 'w') as f:
    for itr in wl:
      f.write(itr+"\n")
      f.write(itr+"?\n")
      f.write(itr+"!\n")
      f.write(itr+"!!\n")
      

change = { 'o' : ["O","0"],
           'a' : ["@"],
           't' : ["7", "T"],
           '1' : ["0", "2"],
           'b' : ["B"], 
           'p' : ["P"] }

wl = ask()
wl = subs(wl, change)
print 'There have been', len(wl), 'possible phrases written to file!'
#filefilefile(wl)
print wl
print len(wl)
print("you were zapped {} times".format(zap))
