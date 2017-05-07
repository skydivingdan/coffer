#import random
#import math


class account(object):
  import datetime 
  def __init__(self, account):
    self.account = { 'account': account , 'created' : self.datetime.date.today() }

  def enterPass(self):
    self.account['password'] = raw_input('What is your password? ')
    self.updateTime()

  def pickWords(self, number):
    delim = raw_input('What goes between the words? ')
    self.account['password'] = pickWords(number,delim)
    self.updateTime()

  def addInfo(self, key):  #This would update too I suppose
    print "What is the value for {}".format(key)
    self.account[key] = raw_input('?> ')

  def pickLetters(self, number):
    self.account['password'] = pickLetters(number)
    self.updateTime()

  def updateTime(self):
    self.account['lastUpdated'] = self.datetime.datetime.today()
    
  def getInfo(self, info):
    if info in self.account.keys():
      i = self.account[info]
    else:
      i = ""
    return i 

  def infoAvail(self):
    for i in self.account.keys():
      print i
  
  def sendToVault(self, vault):
    if self.account['account'] in vault.vault.keys():
      print "This account exist.  Overwrite?"
      if raw_input('?> ') == 'yes':
        vault.vault[self.account['account']] = str(self.account)
      else:
        print "Not updating"
    else:
      vault.vault[self.account['account']] = str(self.account)

  def getFromVault(self, vault, account):
    if account in vault.vault.keys():
      import datetime
      self.account = eval(vault.vault[account])
    else:
      print "{} isn't in that vault {}".format(account,vault)

  def __str__(self):
    return "This is the account information for {}".format(self.account['account'])


class vault(object):
  
  import hashlib, getpass

  def __init__(self):
    self.vault = {}
    #self.name = name
    print "What is this vaults password"
    self.cipher = aescipher(self.hashlib.sha256(self.getpass.getpass('>')).digest()) 

  def __str__(self):
    #return "this is the {} vault".format(self.name)
    self.listVault()

  def readVault(self, file):
    #pass
    # this will be where to read the file with the saved vault
    try:
      with open(file, 'r') as f:
        string = f.read()
    except:
      print "No... just no... That's not a file"
    try:
      self.vault = self.cipher.decrypt(string)
    except:
      print "That appears to be the wrong key"
      print "Try another key"
      self.cipher = aescipher(self.hashlib.sha256(self.getpass.getpass('>')).digest()) 
      self.readVault(file)


  def listVault(self):   ## See what's in the vault
    for account in self.vault.keys():
      print account
    
  def writeVault(self, file):
    string = self.cipher.encrypt(str(self.vault))
    try:
      with open(file, 'w') as f:
        #f.seek(0)
        f.write(string)
        #f.truncate()
    except:
      print "Just no, no, no.... Not a file!"


class aescipher(object):
  import hashlib, base64, getpass
  from Crypto.Cipher import AES
  from Crypto import Random

  def __init__(self, key):
    self.key = key

  def encrypt(self, vault):  #Vault comes in as a dict.  Will leave as a b64 string
    string = str(vault)
    #print string
    bstring = self.base64.b64encode(string)
    #print bstring
    bstring = bstring + '=' * (16 - len(bstring)%16)
    #print len(bstring)%16
    iv = self.Random.new().read(self.AES.block_size)
    #print "Have the IV"
    en = self.AES.new( self.key , self.AES.MODE_CBC , iv )
    return self.base64.b64encode(iv + en.encrypt(bstring))

  def decrypt(self, estring): #Enters as a b64 string will leave as a dict
    e = self.base64.b64decode(estring)
    iv = e[:self.AES.block_size]
    en = self.AES.new( self.key, self.AES.MODE_CBC, iv)
    return eval(self.base64.b64decode(en.decrypt(e[16:])))

#####################################################################

def pickWords(num,delim): ## number of words and a delimiter usually just ' '
  import random
  wl = []
  with open('words.txt','r') as f:
    for line in f:
      wl.append(line.strip())
  s = ''
  while num > 0:
    n = random.randint(0,1)
    m = random.randint(0,len(wl)-1)
    if n == 1:
      s = s + delim + wl[m].lower()
    else:
      s = s + delim  + wl[m]
    num -= 1
  return s[1:]

def pickLetters(num):
  import string
  import random
  s = ''
  print "Full 95 Character set  = 0 (default)"
  print "Letters and Numbers = 1"
  print "Just letters = 2"
  print "Letters + custom = 3"
  print "Letters + numbers + custom = 4"
  pick = raw_input('?>  ')
  if pick == '0' or pick == '':
    cs = string.lowercase + string.uppercase + string.digits + string.punctuation + ' '
  elif pick == '1':
    cs = string.lowercase + string.uppercase + string.digits 
  elif pick == '2':
    cs = string.lowercase + string.uppercase 
  elif pick == '3':
    custom = raw_input('What other characters? ')
    cs = string.lowercase + string.uppercase + custom
  elif pick == '4':  
    custom = raw_input('What other characters? ')
    cs = string.lowercase + string.uppercase + string.digits + custom 
  else:
    print "That's a bold strategy cotton.  Let's see if it pays off"
    cs = "monkey123"
  if cs == 'monkey123':
    return cs
  else:
    while num > 0:
      r = random.randint(0,len(cs)-1)
      s = s + cs[r]
      num -= 1
  return s
 
##################################
def mainLooptyLoop():
  exit = False
  print "\n"*100
  while exit == False:
    print "Welcome to Coffer.  A simple text based password vault"
    print "What to do what to do what to do"
    print "Open a vault, Manage an account, Save vault, Exit?"
    action = raw_input('??>  ') 
    if 'O' in action:
      print "You want to open a vault"
    elif 'M' in action:
      print "You want to manage an account"
    elif 'S' in action:
      print "You want to save the vault"
    elif 'E' in action: 
      print "Exiting" 
      exit = True
    else: 
      print "Fuck you"

  

############################################################################


if __name__ == '__main__':
  mainLooptyLoop()
