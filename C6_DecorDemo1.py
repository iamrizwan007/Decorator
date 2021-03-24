def decor(func):
 def inner():
  print("send the person to beauty parlour")
  print("showing person full of decoration")
 return inner

@decor
def display():
 print("showing a person as it is")

display() #PVM will check for decor, if yes then normal display will not execute, pass normal display as the input function to decor and the return the inner object(after executing)
