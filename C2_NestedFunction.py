def outer():
 print('outer function execution started')
 def inner():
  print('inner function execution')
 inner() #we are calling inner then only it will executed
 print('outer function completed')

outer() #only outer will be executed as inner was not called
#inner() #we cannot call inner function as it is local to the outer(), outside we cannot.
