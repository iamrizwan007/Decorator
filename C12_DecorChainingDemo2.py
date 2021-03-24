#Input-->Facial Decoration-->Hair Decoration-->Dess Decoration-->Output
#f()-->decor1-->inner1-->decor2-->inner2

def decor1(func):
 def inner1():
  print("decor 1 execution")
  func()	#decor input func call -> original function
 return inner1


def decor2(func):
 def inner2():
  print("decor 2 execution")
  func()	#decor input func call -> inner1
 return inner2

@decor2
@decor1
def f():
 print("original funciton")

f()