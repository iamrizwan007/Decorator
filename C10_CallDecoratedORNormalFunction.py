def decor(func):
 def inner(name):
  if name=='sunny':
   print('#'*50)
   print("Hello Sunny, VERY VERY GOOD MORNING")
   print('#'*50)
  else:
   func(name)
 return inner

def wish(name):
 print("good morning",name)

decorated_wish = decor(wish)


decorated_wish('rizwan')
decorated_wish('sunny')