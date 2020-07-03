import random


eins = 0 
zwei = 0 
drei = 0 
vier = 0 
fuenf = 0 
sechs = 0 
for _ in range(100):
  x = random.randint(1,6)
  print(x)
  if x == 1:
    eins +=1
  elif x == 2:
    zwei +=1
  elif x == 3:
    drei +=1
  elif x == 4:
    vier +=1
  elif x == 5:
    fuenf+=1
  elif x == 6:
    sechs +=1
print(eins)
print(zwei)
print(drei)
print(vier)
print(fuenf)
print(sechs)
