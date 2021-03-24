def outer():
 def inner():
  print('inner function execution')
 return inner	#returns inner function objects, return inner() - executed and this function will return something

f1 = outer()	#f1 to hold what outer is returning, in out case inner object
f1() #inner function will be called, f1 internally pointing to f1
