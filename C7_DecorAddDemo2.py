def decor(func):	#add(10,20) will become input
 def inner(a,b):	#a = 10, b = 20 #Must have same arguments
  print("#"*30)
  print('The Sum is:',end='')
  func(a,b)	#original function calling as well for addition
  print('#'*30)
 return inner	#this will execute inner function to return

@decor
def add(a,b):
 print(a+b)

add(10,20)