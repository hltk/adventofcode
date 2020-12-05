u=open('input').readlines()[0].split(',')
for c in u:
   try:
      c = int(c)
      c = chr(c)
      print(c, end='')
   except:
      pass
   
