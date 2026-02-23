import random
import string
a=int(input("length of your password:"))
while(True):
  words=string.ascii_letters+string.digits
  symbols=random.choices("@#$&!")
  b=random.choices(words,k=a-1)  
  passwords=b+symbols
  random.shuffle(passwords)
  password="".join(passwords)
  print("Suggested Password for you:",password) 
  c=int(input("Is the password is ok for you,enter 1 if ok or enter 0 if not ok:"))    
  if(c==1): 
   break