def decor(func):
 def inner(name):
  if name=='sunny':
   print('#'*50)
   print("Hello Sunny, VERY VERY GOOD MORNING")
   print('#'*50)
  else:
   func(name)
 return inner

@decor
def wish(name):
 print("good morning",name)

wish('Rizwan')
wish('sunny')