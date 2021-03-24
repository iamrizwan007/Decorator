def decor(func):
 def inner(a,b):
  if b==0:
   print("Hey Stupid!, How can we divide with zero")
  else:
   func(a,b)
 return inner 

@decor
def division(a,b):
 print(a/b)

division(10,2)
division(10,0)